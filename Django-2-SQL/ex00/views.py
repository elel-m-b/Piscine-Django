import psycopg2

from django.conf import settings
from django.http import HttpResponse


CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS ex00_movies (
        title           VARCHAR(64)     UNIQUE NOT NULL,
        episode_nb      INTEGER         PRIMARY KEY,
        opening_crawl   TEXT,
        director        VARCHAR(32)     NOT NULL,
        producer        VARCHAR(128)    NOT NULL,
        release_date    DATE            NOT NULL
    );
"""


def get_connection():
    """
    Build a psycopg2 connection using the credentials configured in
    Django's settings.py (DATABASES['default']). This keeps a single
    source of truth for DB configuration while still using psycopg2
    directly instead of the Django ORM, as required by the exercise.
    """
    db_settings = settings.DATABASES['default']

    return psycopg2.connect(
        dbname=db_settings.get('NAME'),
        user=db_settings.get('USER'),
        password=db_settings.get('PASSWORD'),
        host=db_settings.get('HOST') or 'localhost',
        port=db_settings.get('PORT') or '5432',
    )


def init(request):
    """
    View reachable at 127.0.0.1:8000/ex00/init

    Creates the ex00_movies table (if it does not already exist) in the
    PostgreSQL database using psycopg2. Returns "OK" on success, or an
    error message describing the problem otherwise.
    """
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        conn.commit()
        cursor.close()

        return HttpResponse("OK")

    except Exception as error:
        return HttpResponse(
            "Error: {}".format(error),
            status=500,
        )

    finally:
        if conn is not None:
            conn.close()
