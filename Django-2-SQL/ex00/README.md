# ex00 — SQL: building a table

## What it does
Exposes a single view, `127.0.0.1:8000/ex00/init`, that connects to
PostgreSQL with `psycopg2` and runs a `CREATE TABLE IF NOT EXISTS` for
`ex00_movies` (title, episode_nb PK, opening_crawl, director, producer,
release_date). Returns `OK` on success, or an error message otherwise.

## How to run
1. Make sure PostgreSQL is running and `djangotraining`/`djangouser` exist
   (see the root `setup.sql`).
2. From the repo root: `python3 manage.py runserver`
3. Visit `http://127.0.0.1:8000/ex00/init`
