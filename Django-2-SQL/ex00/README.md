# ex00 SQL: Building a Table

This Django app exposes one view, reachable at:

    127.0.0.1:8000/ex00/init

It uses `psycopg2` (not the Django ORM) to create the `ex00_movies`
table in PostgreSQL if it does not already exist, then returns "OK".
On failure it returns a 500 response with the error message.

## Table schema

```sql
CREATE TABLE IF NOT EXISTS ex00_movies (
    title           VARCHAR(64)     UNIQUE NOT NULL,
    episode_nb      INTEGER         PRIMARY KEY,
    opening_crawl   TEXT,
    director        VARCHAR(32)     NOT NULL,
    producer        VARCHAR(128)    NOT NULL,
    release_date    DATE            NOT NULL
);
```

## Integration into a Django project

1. Copy the `ex00/` folder into the root of your Django project
   (next to `manage.py`).

2. Add `'ex00'` to `INSTALLED_APPS` in your project's `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'ex00',
   ]
   ```

3. Make sure `settings.py` has a PostgreSQL entry under `DATABASES`
   (host/port/name/user/password), e.g.:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   `ex00/views.py` reads these same settings to open its psycopg2
   connection, so no credentials are duplicated.

4. Include the app's URLs in your project's main `urls.py`:

   ```python
   from django.urls import path, include

   urlpatterns = [
       ...
       path('ex00/', include('ex00.urls')),
   ]
   ```

5. Make sure `psycopg2` (or `psycopg2-binary`) is installed:

   ```bash
   pip install psycopg2-binary
   ```

6. Run the server and visit:

   ```
   http://127.0.0.1:8000/ex00/init
   ```

   You should see "OK" on success.
