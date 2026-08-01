# Ex00: First Static Page

Django project `d05`, application `ex00`, serving a Markdown cheatsheet
at `/ex00`.

## Run it

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd ex00
python3 manage.py migrate
python3 manage.py runserver
```

Visit http://localhost:8000/ex00 (or `/ex00/`, both work).
`/ex00foo` correctly returns a 404.

## Structure

```
requirements.txt
ex00/
├── manage.py
├── d05/            project (settings, root urls, wsgi/asgi)
└── ex00/           application
    ├── urls.py
    ├── views.py
    └── templates/
        └── index.html
```
