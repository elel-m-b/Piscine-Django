# ex02 — SQL: data insertion

## What it does
- `127.0.0.1:8000/ex02/init` — creates `ex02_movies` (same schema as `ex00`).
- `127.0.0.1:8000/ex02/populate` — inserts the 7 Star Wars movies, one `OK`
  line per successful insert (or an error message per failed row).
- `127.0.0.1:8000/ex02/display` — renders all rows as an HTML table, or
  "No data available" if the table is empty/missing.

## How to run
1. Ensure PostgreSQL is up and the DB/role exist.
2. `python3 manage.py runserver`
3. Visit `/ex02/init`, then `/ex02/populate`, then `/ex02/display`.
