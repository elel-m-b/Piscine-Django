# Exercise 05: Hello World (Django)

## Run it

```bash
pip install -r requirements.txt
cd helloworld_project
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

Then open http://localhost:8000/helloworld in your browser: it displays
`Hello World!`.

## Structure

- `helloworld_project/` - the Django project (settings, root urls, wsgi/asgi)
- `helloworld_project/helloworld/` - the Django app defining the `/helloworld`
  view that returns "Hello World!"
