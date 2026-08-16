# ex08 — SQL: Foreign Key

## What it does
- `/ex08/init` — creates `ex08_planets` and `ex08_people`
  (`ex08_people.homeworld` is a `FOREIGN KEY` referencing
  `ex08_planets.name`).
- `/ex08/populate` — bulk-loads `planets.csv` then `people.csv`
  (planets first, since people reference them) using
  `psycopg2.cursor.copy_expert`.
- `/ex08/display` — lists every character's name, homeworld, and climate,
  filtered to planets whose climate is "windy" or "moderately windy",
  sorted alphabetically by character name.

Data files: `people.csv` / `planets.csv` ship in `ex08/data/` (and at the
repo root).

## How to run
1. Ensure PostgreSQL is up and the DB/role exist.
2. `python3 manage.py runserver`
3. Visit `/ex08/init`, then `/ex08/populate`, then `/ex08/display`.
