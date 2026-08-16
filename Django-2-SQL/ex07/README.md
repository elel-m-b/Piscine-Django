# ex07 — ORM: updating data

## What it does
Same as `ex06` through the ORM: a `Movies` model with
`created = DateTimeField(auto_now_add=True)` and
`updated = DateTimeField(auto_now=True)`.
- `/ex07/populate` — inserts the 7 movies.
- `/ex07/display` — HTML table including `created`/`updated`.
- `/ex07/update` — form to edit a movie's `opening_crawl`; saving the model
  automatically refreshes `updated`.

## How to run
1. `python3 manage.py makemigrations && python3 manage.py migrate`
2. `python3 manage.py runserver`
3. Visit `/ex07/populate`, then try `/ex07/update`.
