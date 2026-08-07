from datetime import date

from django.db import connection
from django.db.utils import DatabaseError
from django.http import HttpResponse

from .models import Movies


def init(request):
    """Create the ex02_movies table. Returns 'OK' on success, an error
    message describing the problem otherwise."""
    try:
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Movies)
        return HttpResponse("OK")
    except DatabaseError as error:
        return HttpResponse(f"Error: {error}")


MOVIES_DATA = [
    {
        "episode_nb": 1,
        "title": "The Phantom Menace",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": date(1999, 5, 19),
    },
    {
        "episode_nb": 2,
        "title": "Attack of the Clones",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": date(2002, 5, 16),
    },
    {
        "episode_nb": 3,
        "title": "Revenge of the Sith",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": date(2005, 5, 19),
    },
    {
        "episode_nb": 4,
        "title": "A New Hope",
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": date(1977, 5, 25),
    },
    {
        "episode_nb": 5,
        "title": "The Empire Strikes Back",
        "director": "Irvin Kershner",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": date(1980, 5, 17),
    },
    {
        "episode_nb": 6,
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
        "release_date": date(1983, 5, 25),
    },
    {
        "episode_nb": 7,
        "title": "The Force Awakens",
        "director": "J. J. Abrams",
        "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
        "release_date": date(2015, 12, 11),
    },
]


def populate(request):
    """Insert the seven Star Wars movies into ex02_movies. Displays 'OK'
    for each successful insertion, or an error message otherwise."""
    lines = []
    for movie in MOVIES_DATA:
        try:
            Movies.objects.update_or_create(
                episode_nb=movie["episode_nb"],
                defaults={
                    "title": movie["title"],
                    "director": movie["director"],
                    "producer": movie["producer"],
                    "release_date": movie["release_date"],
                },
            )
            lines.append("OK")
        except DatabaseError as error:
            lines.append(f"Error: {error}")
    return HttpResponse("<br>".join(lines))


def display(request):
    """Display every row of ex02_movies as an HTML table, or
    'No data available' if there is nothing to show / an error occurs."""
    try:
        movies = list(Movies.objects.all().order_by("episode_nb"))
    except DatabaseError:
        return HttpResponse("No data available")

    if not movies:
        return HttpResponse("No data available")

    header = (
        "<tr>"
        "<th>episode_nb</th><th>title</th><th>opening_crawl</th>"
        "<th>director</th><th>producer</th><th>release_date</th>"
        "</tr>"
    )
    rows = ""
    for movie in movies:
        rows += (
            "<tr>"
            f"<td>{movie.episode_nb}</td>"
            f"<td>{movie.title}</td>"
            f"<td>{movie.opening_crawl or ''}</td>"
            f"<td>{movie.director}</td>"
            f"<td>{movie.producer}</td>"
            f"<td>{movie.release_date}</td>"
            "</tr>"
        )
    table = f"<table border=\"1\">{header}{rows}</table>"
    return HttpResponse(table)
