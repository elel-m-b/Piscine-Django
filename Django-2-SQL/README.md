# Django_2_SQL: Django & PostgreSQL: Raw SQL vs ORM

This repo is a single Django project containing eleven independent
exercise apps (`ex00` → `ex10`) that progressively teach the same set of
skills, once by hand with raw SQL (psycopg2) and once through Django's ORM.

## Learning concepts covered today

- **Django project / app structure**: one project, one app per exercise,
  each app self-contained (URLs, views, templates).
- **Raw SQL vs. the ORM**: every "SQL" exercise talks to PostgreSQL directly
  through `psycopg2` (`CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE`, joins);
  every matching "ORM" exercise expresses the same operation with Django
  `Model`s and the QuerySet API — same result, two different tools.
- **Schema design**: primary keys, `UNIQUE` constraints, nullable vs.
  non-nullable columns, and foreign keys (`ex08`/`ex09`/`ex10`).
- **Data loading**: bulk-loading CSV data with `psycopg2`'s `copy_expert`
  (`ex08`), and loading JSON fixtures with Django's `loaddata` management
  command (`ex09`, `ex10`).
- **Forms and mutation**: HTML forms that insert, delete, and update rows,
  both via raw SQL and via the ORM (`ex04`–`ex07`).
- **Triggers vs. `auto_now`/`auto_now_add`**: `ex06` implements a Postgres
  trigger that stamps `updated` on every `UPDATE` while preserving
  `created`; `ex07` reproduces the same behaviour purely through Django
  model fields.
- **Relationships**: one-to-many (`ex08`/`ex09`, people → planets) and
  many-to-many (`ex10`, movies ↔ characters), queried with joins in raw SQL
  and with `select_related`/`ManyToManyField` lookups in the ORM.

## Exercise map

| Exercise | Type | What it does |
|---|---|---|
| `ex00` | SQL | Creates the `ex00_movies` table. |
| `ex01` | ORM | `Movies` model, same schema as `ex00`. |
| `ex02` | SQL | Create + populate + display `ex02_movies`. |
| `ex03` | ORM | Same as `ex02`, via the `Movies` model. |
| `ex04` | SQL | `ex02` + a form to delete a movie by title. |
| `ex05` | ORM | Same as `ex04`, via the ORM. |
| `ex06` | SQL | Adds `created`/`updated` + a Postgres trigger; form to edit `opening_crawl`. |
| `ex07` | ORM | Same as `ex06`, using `auto_now`/`auto_now_add` semantics. |
| `ex08` | SQL | `ex08_planets` / `ex08_people` with a `FOREIGN KEY`, bulk-loaded from CSV via `copy_expert`, joined and filtered by climate. |
| `ex09` | ORM | `Planets` / `People` models loaded via `loaddata`, same "windy climate" query through the ORM. |
| `ex10` | ORM | Adds a `Movies` model with a `characters` `ManyToManyField` to `People`; a search form filters by release-date range, gender, and homeworld diameter. |

Each app also has its own short `README.md` with exact run instructions.

## One-time setup

1. **Install PostgreSQL** and make sure it's running locally on port 5432.
2. **Create the role and database** the project expects
   (`djangotraining` / `djangouser` / `secret`, with full rights):

   ```bash
   sudo -u postgres psql -f setup.sql
   ```

   (`setup.sql` is at the root of this repo and simply runs the
   `CREATE ROLE` / `CREATE DATABASE` / `GRANT` statements described in the
   subject.)

3. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (none are shipped in this repo, as required by the
   subject — they are generated fresh):

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Start the server**:

   ```bash
   python3 manage.py runserver
   ```

   All URLs are then reachable at `127.0.0.1:8000/exXX/...` as described in
   the subject and in each app's README.

## Loading the provided datasets

- `ex08` reads `people.csv` / `planets.csv` (copies are stored in
  `ex08/data/`, and also at the repo root) directly from its `/populate`
  view — no extra step needed beyond calling `127.0.0.1:8000/ex08/populate`.
- `ex09` and `ex10` ship their fixtures inside `ex09/fixtures/` and
  `ex10/fixtures/` respectively. Load them with:

  ```bash
  python3 manage.py loaddata ex09_initial_data.json
  python3 manage.py loaddata ex10_initial_data.json
  ```

  `ex09`'s `/display` view prints this exact command if the table is still
  empty, as required by the subject.

## Implementation notes / deliberate choices

- **Independence between exercises**: per the subject's rules, code that
  repeats across exercises (e.g. the `get_connection()` psycopg2 helper, or
  the `Movies` model definition) is duplicated inside each app rather than
  imported from a shared module.
- **`homeworld` foreign key (`ex09`/`ex10`)**: the subject's text describes
  `homeworld` as "a foreign key referencing the *name* column" of `Planets`.
  The provided `ex09_initial_data.json` / `ex10_initial_data.json`
  fixtures, however, store `homeworld` as the **numeric primary key** of a
  `Planets` row (Django's standard `loaddata` representation of a
  `ForeignKey`). To keep `manage.py loaddata <fixture>.json` working
  out of the box with the data you provided, `homeworld` is implemented as
  a normal `ForeignKey(Planets)` (pointing at `Planets.pk`), not a
  `to_field='name'` FK. Functionally it is still "a foreign key from People
  to Planets", which is the relationship the exercise is testing.
- **`created`/`updated` on `ex09`/`ex10` models**: `auto_now_add`/`auto_now`
  cannot be combined with an explicit `default`, and Django's `loaddata`
  skips a field's `auto_now*` behaviour on raw inserts. Since the `ex10`
  fixture omits `created`/`updated` entirely, plain `default=timezone.now`
  fields are used instead, with a `save()` override that stamps `updated`
  on every subsequent (non-fixture) save — reproducing `auto_now` behaviour
  for normal use while still allowing the fixture to load cleanly.
- **`ex10` diameter filter**: the subject's field label says "diameter
  *greater than*", but its body text clarifies "diameter is greater **or
  equal**" — implemented as `>=` to match the worked example given in the
  subject (diameters of exactly-11000 aren't in the sample data, so both
  readings happen to produce the same example output).
