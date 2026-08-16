# ex03 — ORM: data insertion

## What it does
Same as `ex02` but through the ORM: a `Movies` model identical to `ex01`,
plus:
- `127.0.0.1:8000/ex03/populate` — `get_or_create`s the 7 movies.
- `127.0.0.1:8000/ex03/display` — renders all rows as an HTML table, or
  "No data available".

## How to run
1. `python3 manage.py makemigrations && python3 manage.py migrate`
2. `python3 manage.py runserver`
3. Visit `/ex03/populate`, then `/ex03/display`.
