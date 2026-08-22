from django.conf import settings
from django.db import models


class ChatRoom(models.Model):
    """A chatroom. Its name is what shows up in the room list and is
    also used (URL-encoded) as part of the room's URL."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Message(models.Model):
    """A single message posted by a user in a chatroom. Kept forever, in
    posting order, so we can show history to new visitors (Exercise 02)."""

    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content[:30]}'
