# ex04 — SQL: data deleting

## What it does
- `/ex04/init` — creates `ex04_movies`.
- `/ex04/populate` — (re)inserts the 7 movies; re-running it restores any
  row you previously removed.
- `/ex04/display` — HTML table of all rows, or "No data available".
- `/ex04/remove` — a form with a dropdown of titles; submitting it deletes
  the selected movie and redisplays the form with the updated list.

## How to run
1. Ensure PostgreSQL is up and the DB/role exist.
2. `python3 manage.py runserver`
3. Visit `/ex04/init`, `/ex04/populate`, then try `/ex04/remove`.
