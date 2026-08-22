// Exercises 01-04: the chat itself, driven entirely by WebSockets (no
// AJAX here) plus jQuery as the only frontend library.
$(function () {
    const roomName = JSON.parse($('#room-name').text());
    const currentUsername = JSON.parse($('#current-username').text());

    const $chatLog = $('#chat-log');
    const $userList = $('#user-list');
    const $form = $('#chat-form');
    const $input = $('#chat-message-input');

    const wsScheme = (window.location.protocol === 'https:') ? 'wss' : 'ws';
    const chatSocket = new WebSocket(
        wsScheme + '://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    function scrollToBottom() {
        // Exercise 04: always keep the newest message in view.
        $chatLog.scrollTop($chatLog[0].scrollHeight);
    }

    function appendChatMessage(username, message) {
        const isMe = (username === currentUsername);
        const $line = $('<div class="mb-1"></div>');
        $('<strong></strong>').text(username + ': ').appendTo($line);
        $('<span></span>').text(message).appendTo($line);
        if (isMe) {
            $line.addClass('text-primary');
        }
        $chatLog.append($line);
        scrollToBottom();
    }

    function appendSystemMessage(message) {
        const $line = $('<div class="text-muted fst-italic small mb-1"></div>').text(message);
        $chatLog.append($line);
        scrollToBottom();
    }

    function renderUserList(users) {
        $userList.empty();
        $.each(users, function (_, username) {
            const $item = $('<li class="list-group-item py-1"></li>').text(username);
            if (username === currentUsername) {
                $item.addClass('fw-bold');
            }
            $userList.append($item);
        });
    }

    chatSocket.onmessage = function (event) {
        const data = JSON.parse(event.data);

        if (data.type === 'chat_message') {
            appendChatMessage(data.username, data.message);
        } else if (data.type === 'system') {
            appendSystemMessage(data.message);
        } else if (data.type === 'user_list') {
            renderUserList(data.users);
        }
    };

    chatSocket.onclose = function () {
        appendSystemMessage('Connection closed.');
    };

    $form.on('submit', function (event) {
        event.preventDefault();
        const message = $input.val().trim();
        if (!message) {
            return;
        }
        chatSocket.send(JSON.stringify({ message: message }));
        $input.val('').focus();
    });
});
