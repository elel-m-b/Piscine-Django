# ex06 — SQL: updating data

## What it does
- `/ex06/init` — creates `ex06_movies` (same schema + `created`/`updated`
  timestamps) and installs the Postgres trigger from the subject that sets
  `updated = now()` and keeps `created` unchanged on every `UPDATE`.
- `/ex06/populate` — inserts the 7 movies.
- `/ex06/display` — HTML table including `created`/`updated`.
- `/ex06/update` — a form to pick a movie and overwrite its
  `opening_crawl`; the trigger bumps `updated` automatically.

## How to run
1. Ensure PostgreSQL is up and the DB/role exist.
2. `python3 manage.py runserver`
3. Visit `/ex06/init`, `/ex06/populate`, then try `/ex06/update`.
