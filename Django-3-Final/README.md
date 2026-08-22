#Django-3-Final

Django project for the **Python-Django - 3 Final** subject.

The project contains 5 exercises:

* AJAX login/logout
* Basic WebSocket chat
* Chat history
* Online user list
* Auto-scroll chat

## Project structure

```text
ex/
├── manage.py
├── requirements.txt
│
├── d09/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── account/
│   ├── views.py
│   └── urls.py
│
├── chat/
│   ├── models.py
│   ├── views.py
│   ├── consumers.py
│   ├── routing.py
│   ├── urls.py
│   └── fixtures/
│       └── rooms.json
│
├── templates/
│   ├── base.html
│   ├── account/
│   │   └── account.html
│   └── chat/
│       ├── room_list.html
│       └── room_detail.html
│
└── static/
    └── js/
        ├── csrf.js
        ├── account.js
        └── chat.js
```

## Requirements

* Python 3.10+
* pip
* Internet connection

Main technologies:

* Django
* Django Channels
* Daphne
* SQLite
* jQuery
* WebSockets
* Bootstrap

The project uses `InMemoryChannelLayer`, which is enough for local development.

## Installation

```bash
cd ex

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Create the database:

```bash
python3 manage.py migrate
```

Load the chatrooms:

```bash
python3 manage.py loaddata chat/fixtures/rooms.json
```

Create a user:

```bash
python3 manage.py createsuperuser
```

Run the project:

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

## Exercises

### Exercise 00 — AJAX Login / Logout

Login and logout are handled using AJAX.

* No page reload after login.
* No page reload after logout.
* Django `AuthenticationForm` is used for authentication.
* AJAX requests return JSON.
* CSRF protection is handled in `csrf.js`.

Test:

1. Open `/account/`.
2. Try an incorrect password.
3. Login with valid credentials.
4. Logout.
5. Refresh the page and check that the session is preserved.

### Exercise 01 — Basic Chat

The project contains three chatrooms:

* General
* Movies
* Gaming

Chat uses WebSockets through Django Channels.

Only authenticated users can enter a room.

Test with two browser sessions:

```text
Browser 1 → Alice
Browser 2 → Bob
```

Join the same room and send messages between them.

### Exercise 02 — Chat History

When joining a room, the last **3 messages** are displayed.

Messages are shown from oldest to newest.

### Exercise 03 — User List

Each room has a list of connected users.

The list is updated when:

* A user joins.
* A user leaves.

The online user list is kept in memory and is not stored in the database.

### Exercise 04 — Auto Scroll

The chat message area has a fixed height and becomes scrollable when there are many messages.

New messages automatically scroll the chat to the bottom.

## Testing

A simple test:

1. Start the server.
2. Open `/account/`.
3. Login as a user.
4. Open a chatroom.
5. Open another browser/private window.
6. Login with another user.
7. Join the same room.
8. Send messages.
9. Check the user list.
10. Close one browser and check that the user disappears.
11. Send enough messages to test scrolling.

## Troubleshooting

| Problem                       | Solution                                              |
| ----------------------------- | ----------------------------------------------------- |
| Django is not installed       | `pip install -r requirements.txt`                     |
| Database table does not exist | `python3 manage.py migrate`                           |
| No chatrooms                  | `python3 manage.py loaddata chat/fixtures/rooms.json` |
| AJAX returns 403              | Check CSRF and cookies                                |
| WebSocket does not connect    | Make sure you are logged in and the server is running |
| User list does not update     | Refresh and reconnect the WebSocket                   |

## Demo

If the provided fixtures contain the demo users:

```text
Username: alice
Password: d09testpass

Username: bob
Password: d09testpass
```

Use two different browser sessions to test the chat.

## Author

Training project — Python/Django.
