# ex10 — ORM: Many to Many

## What it does
`Planets`, `People` (identical to `ex09`) plus `Movies`
(identical to `ex01` + a `characters` `ManyToManyField(People)`).

`127.0.0.1:8000/ex10/` shows a form (min/max release date, minimum planet
diameter, character gender) and, once submitted, lists every
character/movie/homeworld combination matching all four filters — or
"Nothing corresponding to your research" if none match.

Fixture: `ex10/fixtures/ex10_initial_data.json`.

## How to run
1. `python3 manage.py makemigrations && python3 manage.py migrate`
2. `python3 manage.py loaddata ex10_initial_data.json`
3. `python3 manage.py runserver`
4. Visit `/ex10/` and submit the search form.
