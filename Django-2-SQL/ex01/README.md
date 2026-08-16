# ex01 — ORM: building a table

## What it does
Defines a Django model `Movies` (title, episode_nb PK, opening_crawl,
director, producer, release_date) with a `__str__` returning the title.
No views are required by the subject for this exercise.

## How to run
1. `python3 manage.py makemigrations && python3 manage.py migrate`
2. Use `python3 manage.py shell` or the admin site to inspect the model.
