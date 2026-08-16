import psycopg2
from django.conf import settings
from django.http import HttpResponse


def get_connection():
    """Open a raw psycopg2 connection using the project's DB settings."""
    db = settings.DATABASES['default']
    return psycopg2.connect(
        dbname=db['NAME'],
        user=db['USER'],
        password=db['PASSWORD'],
        host=db['HOST'],
        port=db['PORT'],
    )


CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS ex00_movies (
    title varchar(64) UNIQUE NOT NULL,
    episode_nb integer PRIMARY KEY,
    opening_crawl text NULL,
    director varchar(32) NOT NULL,
    producer varchar(128) NOT NULL,
    release_date date NOT NULL
);
"""


def init(request):
    """127.0.0.1:8000/ex00/init"""
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)
        conn.commit()
        return HttpResponse("OK")
    except Exception as exc:
        if conn is not None:
            conn.rollback()
        return HttpResponse(f"Error: {exc}")
    finally:
        if conn is not None:
            conn.close()
