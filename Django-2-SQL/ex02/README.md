# ex02 ORM: Reading & Writing Data via Views

A Django app called **ex02** exposing three views (`/ex02/init`,
`/ex02/populate`, `/ex02/display`) that create, fill, and read a table
named `ex02_movies`, wired into a minimal Django project
(`django_project`) so it can be run directly.

## Project layout

```
.
├── manage.py
├── django_project/          # minimal Django project (settings, urls, wsgi/asgi)
│   ├── settings.py           # ex02 is registered in INSTALLED_APPS here
│   └── urls.py                # includes ex02.urls under /ex02/
└── ex02/
    ├── models.py              # Movies model, Meta.db_table = "ex02_movies"
    ├── views.py                # init / populate / display views
    ├── urls.py                 # maps init, populate, display to the views
    ├── apps.py
    └── migrations/
        └── __init__.py         # deliberately empty — see "Why no migration file" below
```

If you already have a Django project from earlier exercises, you only
need the `ex02/` folder: drop it next to your other apps, add `'ex02'`
to `INSTALLED_APPS`, and add `path('ex02/', include('ex02.urls'))` to
your project's `urls.py`.

## The three views

`ex02/views.py`:

- **`init`** — creates the `ex02_movies` table by asking Django's schema
  editor to build it straight from the `Movies` model
  (`schema_editor.create_model(Movies)`), no migration file involved.
  Returns `"OK"` on success, or `"Error: ..."` describing the problem
  (e.g. calling it twice returns `Error: table "ex02_movies" already
  exists`).
- **`populate`** — inserts the 7 given movies via
  `Movies.objects.update_or_create(...)`, one call per movie, printing
  `"OK"` per successful insertion (separated by `<br>`), or an error
  message for any that fail.
- **`display`** — reads every row of `ex02_movies` with
  `Movies.objects.all()` and renders it as an HTML `<table>`, including
  empty fields (e.g. `opening_crawl`, which is never populated by
  `populate`, shows up as an empty cell). If the table doesn't exist yet,
  is empty, or a database error occurs, it prints `"No data available"`.

## The `Movies` model

Same field specification as `ex01`'s `Movies`, just mapped to a
different table name via `Meta.db_table`:

```python
class Movies(models.Model):
    title = models.CharField(unique=True, max_length=64, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    class Meta:
        db_table = 'ex02_movies'

    def __str__(self):
        return self.title
```

### Why no migration file for `ex02`

The exercise wants the **`/ex02/init` view itself** to be the thing that
creates the table — visiting `/ex02/display` before hitting `/ex02/init`
should report `"No data available"` because the table genuinely doesn't
exist yet, not because it's just empty. If `ex02_movies` were created by
a normal migration (applied via `python3 manage.py migrate`), the table
would already exist before anyone ever visited `/ex02/init`, which
defeats the point of the exercise.

So `ex02/migrations/` only contains the empty `__init__.py` that Django
requires for the app to be recognized as an app with migrations — no
`0001_initial.py`. The table is created on demand, inside the `init`
view, using `connection.schema_editor().create_model(Movies)`, which
builds exactly the table Django would have generated from the model
without needing a migration file for it.

## Requirements

- Python 3
- Django (`pip install django`)

## How to run it

From the root of this project (the folder containing `manage.py`):

```bash
# 1. install Django if you don't already have it
pip install django

# 2. apply the *project's* base migrations (admin, auth, sessions, ...)
#    this does NOT create ex02_movies — see explanation above
python3 manage.py migrate

# 3. run the dev server
python3 manage.py runserver
```

Then, in order, visit:

```
http://127.0.0.1:8000/ex02/init        -> OK
http://127.0.0.1:8000/ex02/populate    -> OK (x7)
http://127.0.0.1:8000/ex02/display     -> HTML table with all 7 movies
```

Visiting `/ex02/display` before `/ex02/init` shows `No data available`.
Visiting `/ex02/init` a second time shows an error message, since the
table already exists.

## How this was tested

The whole flow was run end-to-end with `curl` against a local dev server
before packaging:

```bash
curl 127.0.0.1:8000/ex02/display    # -> No data available
curl 127.0.0.1:8000/ex02/init       # -> OK
curl 127.0.0.1:8000/ex02/init       # -> Error: table "ex02_movies" already exists
curl 127.0.0.1:8000/ex02/populate   # -> OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK
curl 127.0.0.1:8000/ex02/display    # -> <table>...7 rows, opening_crawl empty...</table>
```

## What this exercise teaches

- **Views as thin controllers.** A Django view is just a function (or
  class) that takes a request and returns an `HttpResponse` — here each
  view's whole job is to talk to the ORM and translate the result into a
  simple text/HTML response.
- **Programmatic schema creation.** Beyond migrations, Django exposes a
  lower-level API (`connection.schema_editor()`) that can create, alter,
  or delete a table for a given model directly — useful when you want
  table creation to be an explicit, on-demand action rather than
  something `migrate` does for you upfront.
- **`update_or_create`.** A safe way to insert-or-update a row keyed on
  a natural key (`episode_nb` here) without manually checking existence
  first or crashing on a duplicate primary key.
- **Routing with `include()`.** Splitting URLs into a per-app `urls.py`
  and mounting it under a prefix (`path('ex02/', include('ex02.urls'))`)
  keeps each app's routes self-contained.
- **Defensive error handling.** Every view catches database errors and
  turns them into a readable message instead of letting a 500 page leak
  a stack trace to the user.
