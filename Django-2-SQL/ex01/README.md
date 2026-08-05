# ORM: Building a Table

This project contains a Django app named `ex01` with a `Movies` model.

## Project structure

```text
|ex01
├── manage.py
├── django_project/
└── ex01/
    ├── models.py
    ├── admin.py
    ├── apps.py
    └── migrations/
```

## Movies model

The `Movies` model has the following fields:

- `title` (unique, max 64 characters)
- `episode_nb` (primary key)
- `opening_crawl` (optional)
- `director` (max 32 characters)
- `producer` (max 128 characters)
- `release_date` (date)

The `__str__()` method returns the movie title.

## Run the project

Install Django:

```bash
pip install django
```

Apply migrations:

```bash
python3 manage.py migrate
```

Run the server:

```bash
python3 manage.py runserver
```

## Test the model

Open the Django shell:

```bash
python3 manage.py shell
```

Example:

```python
from ex01.models import Movies
from datetime import date

movie = Movies(
    title="A New Hope",
    episode_nb=4,
    director="George Lucas",
    producer="Gary Kurtz",
    release_date=date(1977, 5, 25),
)

movie.save()
print(movie)
```