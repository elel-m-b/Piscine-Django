import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
PLANETS_CSV = APP_DIR / 'data' / 'planets.csv'
PEOPLE_CSV = APP_DIR / 'data' / 'people.csv'


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


CREATE_PLANETS_SQL = """
CREATE TABLE IF NOT EXISTS ex08_planets (
    id serial PRIMARY KEY,
    name varchar(64) UNIQUE NOT NULL,
    climate varchar(255),
    diameter integer,
    orbital_period integer,
    population bigint,
    rotation_period integer,
    surface_water real,
    terrain varchar(128)
);
"""

CREATE_PEOPLE_SQL = """
CREATE TABLE IF NOT EXISTS ex08_people (
    id serial PRIMARY KEY,
    name varchar(64) UNIQUE NOT NULL,
    birth_year varchar(32),
    gender varchar(32),
    eye_color varchar(32),
    hair_color varchar(32),
    height integer,
    mass real,
    homeworld varchar(64) REFERENCES ex08_planets(name)
);
"""


def init(request):
    """127.0.0.1:8000/ex08/init"""
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(CREATE_PLANETS_SQL)
            cur.execute(CREATE_PEOPLE_SQL)
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
    """127.0.0.1:8000/ex08/populate -- bulk loads planets.csv then people.csv via copy_expert."""
    conn = None
    lines = []
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            # Planets must be loaded first: people.homeworld references planets.name.
            try:
                with open(PLANETS_CSV) as f:
                    cur.copy_expert(
                        "COPY ex08_planets (name, climate, diameter, orbital_period, "
                        "population, rotation_period, surface_water, terrain) "
                        "FROM STDIN WITH (FORMAT csv, DELIMITER E'\\t', NULL 'NULL')",
                        f,
                    )
                conn.commit()
                lines.append("OK")
            except Exception as exc:
                conn.rollback()
                lines.append(f"Error: {exc}")

            try:
                with open(PEOPLE_CSV) as f:
                    cur.copy_expert(
                        "COPY ex08_people (name, birth_year, gender, eye_color, "
                        "hair_color, height, mass, homeworld) "
                        "FROM STDIN WITH (FORMAT csv, DELIMITER E'\\t', NULL 'NULL')",
                        f,
                    )
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


def display(request):
    """127.0.0.1:8000/ex08/display"""
    conn = None
    rows = []
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT p.name, p.homeworld, pl.climate "
                "FROM ex08_people p "
                "JOIN ex08_planets pl ON p.homeworld = pl.name "
                "WHERE pl.climate ILIKE %s "
                "ORDER BY p.name ASC;",
                ('%windy%',),
            )
            rows = cur.fetchall()
    except Exception:
        rows = []
    finally:
        if conn is not None:
            conn.close()

    if not rows:
        return HttpResponse("No data available")

    return render(request, 'ex08/display.html', {'people': rows})
