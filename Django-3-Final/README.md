# Django-3-Final

This project is about learning **AJAX and WebSockets with Django**.

We will build one Django website step by step.

The final website will have:

* Login / Logout with AJAX
* 3 chat rooms
* Real-time chat with WebSockets
* Message history
* Connected users list
* Automatic chat scrolling

Do not build everything at once.

Complete each step, test it, then continue.

---

# 1. What We Need

Install:

* Python 3
* Django
* Django Channels
* jQuery
* Git

The project must run inside a virtual machine.

Only **jQuery** is allowed as a JavaScript library.

Keep Django's default admin application.

---

# 2. Create the Project

Start by creating a folder:

```bash
mkdir Django-3-final
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Django and Channels:

```bash
pip install django channels
```

Create the Django project:

```bash
django-admin startproject d09 .
```

Create the applications:

```bash
python manage.py startapp account
python manage.py startapp chat
```

Run the server:

```bash
python manage.py migrate
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

If Django works, continue.

---

# 3. Exercise 00 - AJAX Login

First, build authentication.

Create the `account` application.

Create:

```text
/account/
```

This page has two states.

### User is NOT logged in

Show:

```text
Login
Password
[Login]
```

The login must use:

```text
AJAX + POST
```

There must be **no page refresh**.

If the login is wrong:

* Show the error on the page
* Do not refresh the page

If the login is correct:

```text
Logged as username
[Logout]
```

must appear.

### User IS logged in

Show:

```text
Logged as username
[Logout]
```

Logout must also use:

```text
AJAX + POST
```

Again, no page refresh.

### What to learn

* Django authentication
* `AuthenticationForm`
* Django sessions
* AJAX
* POST requests
* JSON responses
* jQuery

### Test

Before continuing, verify:

```text
[ ] Login works
[ ] Wrong login shows an error
[ ] Login does not refresh the page
[ ] Logged username appears
[ ] Logout works
[ ] Logout does not refresh the page
[ ] Refreshing the browser keeps the correct login state
```

---

# 4. Exercise 01 - Basic Chat

Now create the chat application.

We need **3 chat rooms**.

The rooms must be stored in the database.

For example:

```text
Room 1
Room 2
Room 3
```

The home page should show links to the rooms.

Example:

```text
Chat Rooms

[Room 1]
[Room 2]
[Room 3]
```

A user must be logged in before entering a room.

---

## Create the Chat Models

Create a `Room` model.

Create a `Message` model.

A message should contain at least:

```text
user
room
message
timestamp
```

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 5. Configure WebSockets

Now we need to make Django understand WebSockets.

Install/use:

```text
Django Channels
```

Configure:

```text
settings.py
asgi.py
routing.py
consumers.py
```

The basic flow will be:

```text
Browser
   |
   | WebSocket
   v
Django Channels
   |
   v
Consumer
   |
   v
Chat Room
```

Do not worry about the complete chat yet.

First make sure a WebSocket connection can be opened.

---

# 6. Make the Chat Work

Inside a room, create a simple chat interface.

Example:

```text
Room 1

-------------------------
Alice: Hello
Bob: Hi
Alice: How are you?
-------------------------

[Write message................] [Send]
```

When a user sends a message:

```text
Browser
   |
   | WebSocket
   v
Consumer
   |
   v
Database
   |
   v
Other connected users
```

The message must appear for everyone in the same room.

Do NOT use AJAX for the chat.

Use:

```text
WebSockets + jQuery
```

---

# 7. Join Message

When a user enters a room, send:

```text
<username> has joined the chat
```

Example:

```text
Alice has joined the chat
```

Everyone in the room must see it.

The user who joined must also see it.

Test with two browser windows.

Example:

```text
Browser 1: Alice
Browser 2: Bob
```

When Bob joins:

```text
Bob has joined the chat
```

must appear in both browsers.

---

# 8. Exercise 02 - Message History

Now add history.

When a user enters a room, show the **last 3 messages**.

Example database:

```text
Message 1
Message 2
Message 3
Message 4
Message 5
```

New user should see:

```text
Message 3
Message 4
Message 5
```

They must appear:

```text
oldest
   ↓
newest
```

Continue using:

```text
WebSockets + jQuery
```

---

# 9. Exercise 03 - Connected Users

Now add a user list.

The page should look something like:

```text
---------------------------------------
| Messages          | Users           |
|                   |                 |
| Alice: Hello      | Alice           |
| Bob: Hi           | Bob             |
|                   | Charlie         |
---------------------------------------
```

When a user joins:

```text
User joins
    ↓
Add user to list
    ↓
Update everyone
```

When a user leaves:

```text
User leaves
    ↓
Remove user from list
    ↓
Update everyone
```

Also display:

```text
<username> has left the chat
```

Example:

```text
Bob has left the chat
```

---

# 10. Exercise 04 - Scroll

Now make the chat easier to use.

The message area must have a fixed height.

Example:

```text
-------------------------
Alice: Hello
Bob: Hi
Alice: How are you?
Bob: Fine
...
...
-------------------------
          ↓
       scrollbar
```

When new messages arrive:

```text
scroll = bottom
```

The newest message should always be visible.

---

# 11. Final Project Structure

Your project should end up approximately like this:

```text
django-3-final/
│
├── venv/
│
├── manage.py
├── requirements.txt
│
├── d09/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── ...
│
├── account/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── chat/
│   ├── models.py
│   ├── views.py
│   ├── consumers.py
│   ├── routing.py
│   └── ...
│
├── templates/
│
├── static/
│
└── README.md
```

The exact structure can change while you are building the project.

---

# 12. What You Should Understand

By the end of the project, you should understand:

```text
Django
├── Project
├── Apps
├── URLs
├── Views
├── Templates
├── Models
├── ORM
└── Authentication

AJAX
├── GET / POST
├── jQuery
└── JSON

WebSockets
├── Connection
├── Consumer
├── Routing
├── Groups
└── Real-time messages

Django Channels
└── WebSocket support
```

---

# 13. Testing

Do not wait until the end to test.

After every exercise, test it.

## Exercise 00

```text
[ ] Login works
[ ] Logout works
[ ] Wrong credentials show an error
[ ] No page refresh
[ ] Refresh keeps the correct state
```

## Exercise 01

```text
[ ] 3 rooms exist
[ ] Rooms are stored in database
[ ] Only logged users can chat
[ ] WebSocket connection works
[ ] Messages are real-time
[ ] Multiple users can chat
[ ] Messages stay in order
[ ] Join message works
```

## Exercise 02

```text
[ ] Last 3 messages are displayed
[ ] Messages are in the correct order
```

## Exercise 03

```text
[ ] Connected users are displayed
[ ] New users appear automatically
[ ] Users disappear when they leave
[ ] Join message works
[ ] Leave message works
```

## Exercise 04

```text
[ ] Message container has fixed size
[ ] Scrollbar appears
[ ] Scroll stays at the bottom
[ ] New messages are visible
```

---

# 14. Final Step

When everything works:

Create the requirements file:

```bash
pip freeze > requirements.txt
```

Check the project:

```bash
python manage.py check
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

---

# 15. The Important Rule

Do not try to understand the whole project before starting.

Fol
---

# 15. The Important Rule

Do not try to understand the whole project before starting.

Follow this order:

```text
Exercise 00
AJAX Login
     ↓
Exercise 01
Basic WebSocket Chat
     ↓
Exercise 02
Message History
     ↓
Exercise 03
Connected Users
     ↓
Exercise 04
Scroll
     ↓
Final Testing
```

**Build → Test → Understand → Continue.**

