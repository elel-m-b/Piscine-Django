import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import ChatRoom, Message

# In-memory record of who is currently connected to each room, e.g.
# {"General": {"alice", "bob"}}. This lives in normal Python memory (not
# the database) because it's *live, transient* state - it's rebuilt every
# time the server restarts, which is exactly what we want for "who is
# online right now". It works because the development server (Daphne)
# runs as a single process, so every consumer shares this same module.
_connected_users = {}


def _add_user(room_name, username):
    _connected_users.setdefault(room_name, set()).add(username)
    return sorted(_connected_users[room_name])


def _remove_user(room_name, username):
    _connected_users.setdefault(room_name, set()).discard(username)
    return sorted(_connected_users[room_name])


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Handles one visitor's WebSocket connection to one chatroom.

    Message "types" sent down to the browser (see chat.js for how each is
    handled):
      * "chat_message" - someone posted a message (also used for history).
      * "system"       - "<user> has joined/left the chat".
      * "user_list"    - the full, current list of connected usernames.
    """

    async def connect(self):
        self.user = self.scope['user']

        # Exercise 01: "It's only available to connected users."
        if not self.user.is_authenticated:
            await self.close()
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        room_exists = await self.room_exists()
        if not room_exists:
            await self.close()
            return

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Exercise 02: send the last 3 messages (oldest to newest) to this
        # user only (not the whole room) as soon as they connect.
        for message in await self.get_history():
            await self.send(text_data=json.dumps({
                'type': 'chat_message',
                'username': message['username'],
                'message': message['content'],
            }))

        # Exercise 03: register this user as connected, then broadcast the
        # join notice and the fresh userlist to everyone in the room
        # (including the user who just joined).
        users = _add_user(self.room_name, self.user.username)

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat.join',
            'username': self.user.username,
        })
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat.userlist',
            'users': users,
        })

    async def disconnect(self, close_code):
        if not getattr(self, 'room_group_name', None):
            return

        users = _remove_user(self.room_name, self.user.username)

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Exercise 03: tell everyone still in the room that this user left,
        # and share the updated userlist.
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat.leave',
            'username': self.user.username,
        })
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat.userlist',
            'users': users,
        })

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = (data.get('message') or '').strip()
        if not message:
            return

        await self.save_message(message)

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat.message',
            'username': self.user.username,
            'message': message,
        })

    # --- group event handlers: one per "type" used with group_send() above ---

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'username': event['username'],
            'message': event['message'],
        }))

    async def chat_join(self, event):
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': f"{event['username']} has joined the chat",
        }))

    async def chat_leave(self, event):
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': f"{event['username']} has left the chat",
        }))

    async def chat_userlist(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': event['users'],
        }))

    # --- small database helpers (the ORM is synchronous, Channels is not) ---

    @database_sync_to_async
    def room_exists(self):
        return ChatRoom.objects.filter(name=self.room_name).exists()

    @database_sync_to_async
    def save_message(self, content):
        room = ChatRoom.objects.get(name=self.room_name)
        Message.objects.create(room=room, user=self.user, content=content)

    @database_sync_to_async
    def get_history(self):
        room = ChatRoom.objects.get(name=self.room_name)
        last_messages = list(
            room.messages.select_related('user').order_by('-timestamp')[:3]
        )
        last_messages.reverse()  # oldest to newest, as required
        return [
            {'username': m.user.username, 'content': m.content}
            for m in last_messages
        ]
