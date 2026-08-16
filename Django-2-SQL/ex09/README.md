# ex09 — ORM: Foreign Key

## What it does
`Planets` and `People` models (People.homeworld is a ForeignKey to
Planets — see the root README for the exact rationale/caveat about this
FK). `/ex09/display` lists characters + homeworld + climate for "windy"
planets, sorted by name. If the tables are empty it prints the exact
`loaddata` command to run.

Fixture: `ex09/fixtures/ex09_initial_data.json`.

## How to run
1. `python3 manage.py makemigrations && python3 manage.py migrate`
2. `python3 manage.py loaddata ex09_initial_data.json`
3. `python3 manage.py runserver`
4. Visit `/ex09/display`.
