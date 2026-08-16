import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


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
CREATE TABLE IF NOT EXISTS ex06_movies (
    title varchar(64) UNIQUE NOT NULL,
    episode_nb integer PRIMARY KEY,
    opening_crawl text NULL,
    director varchar(32) NOT NULL,
    producer varchar(128) NOT NULL,
    release_date date NOT NULL,
    created timestamp NOT NULL DEFAULT now(),
    updated timestamp NOT NULL DEFAULT now()
);
"""

CREATE_TRIGGER_FUNCTION_SQL = """
CREATE OR REPLACE FUNCTION update_changetimestamp_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated = now();
    NEW.created = OLD.created;
    RETURN NEW;
END;
$$ language 'plpgsql';
"""

DROP_TRIGGER_SQL = "DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies;"

CREATE_TRIGGER_SQL = """
CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
update_changetimestamp_column();
"""

MOVIES = [
    (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
    (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
    (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
    (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
    (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
    (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
    (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
]

INSERT_SQL = """
INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (episode_nb) DO NOTHING;
"""


def init(request):
    """127.0.0.1:8000/ex06/init"""
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)
            cur.execute(CREATE_TRIGGER_FUNCTION_SQL)
            cur.execute(DROP_TRIGGER_SQL)
            cur.execute(CREATE_TRIGGER_SQL)
        conn.commit()
        return HttpResponse("OK")
    except Exception as exc:
        if conn is not None:
            conn.rollback()
        return HttpResponse(f"Error: {exc}")
    finally:
        if conn is not None:
            conn.close()


def populate(request):
    """127.0.0.1:8000/ex06/populate"""
    conn = None
    lines = []
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            for episode_nb, title, director, producer, release_date in MOVIES:
                try:
                    cur.execute(INSERT_SQL, (episode_nb, title, director, producer, release_date))
                    conn.commit()
                    lines.append("OK")
                except Exception as exc:
                    conn.rollback()
                    lines.append(f"Error: {exc}")
    except Exception as exc:
        lines.append(f"Error: {exc}")
    finally:
        if conn is not None:
            conn.close()
    return HttpResponse("<br>".join(lines))


def _fetch_all():
    conn = None
    rows = []
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT episode_nb, title, opening_crawl, director, producer, "
                "release_date, created, updated FROM ex06_movies ORDER BY episode_nb;"
            )
            rows = cur.fetchall()
    except Exception:
        rows = []
    finally:
        if conn is not None:
            conn.close()
    return rows


def display(request):
    """127.0.0.1:8000/ex06/display"""
    rows = _fetch_all()
    if not rows:
        return HttpResponse("No data available")
    return render(request, 'ex06/display.html', {'movies': rows})


def update(request):
    """127.0.0.1:8000/ex06/update"""
    if request.method == 'POST':
        title = request.POST.get('title')
        opening_crawl = request.POST.get('opening_crawl', '')
        if title:
            conn = None
            try:
                conn = get_connection()
                with conn.cursor() as cur:
                    cur.execute(
                        "UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s;",
                        (opening_crawl, title),
                    )
                conn.commit()
            except Exception:
                if conn is not None:
                    conn.rollback()
            finally:
                if conn is not None:
                    conn.close()

    rows = _fetch_all()
    if not rows:
        return HttpResponse("No data available")

    titles = [row[1] for row in rows]
    return render(request, 'ex06/update.html', {'titles': titles})
