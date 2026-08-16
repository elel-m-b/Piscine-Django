# ex05 — ORM: deleting data

## What it does
Same as `ex04`, through the ORM (its own `Movies` model):
- `/ex05/populate` — `update_or_create`s the 7 movies (reinserts removed ones).
- `/ex05/display` — HTML table, or "No data available".
- `/ex05/remove` — dropdown form to delete a movie by title.

## How to run
1. `python3 manage.py makemigrations && python3 manage.py migrate`
2. `python3 manage.py runserver`
3. Visit `/ex05/populate`, then `/ex05/remove`.
