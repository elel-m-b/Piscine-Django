from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

from .models import Movies

MOVIES = [
    (1, "The Phantom Menace", "George Lucas", "Rick McCallum", date(1999, 5, 19)),
    (2, "Attack of the Clones", "George Lucas", "Rick McCallum", date(2002, 5, 16)),
    (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", date(2005, 5, 19)),
    (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", date(1977, 5, 25)),
    (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", date(1980, 5, 17)),
    (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", date(1983, 5, 25)),
    (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", date(2015, 12, 11)),
]


def populate(request):
    """127.0.0.1:8000/ex05/populate -- reinserts any previously removed rows."""
    lines = []
    for episode_nb, title, director, producer, release_date in MOVIES:
        try:
            Movies.objects.update_or_create(
                episode_nb=episode_nb,
                defaults={
                    'title': title,
                    'director': director,
                    'producer': producer,
                    'release_date': release_date,
                },
            )
            lines.append("OK")
        except Exception as exc:
            lines.append(f"Error: {exc}")
    return HttpResponse("<br>".join(lines))


def display(request):
    """127.0.0.1:8000/ex05/display"""
    movies = Movies.objects.all().order_by('episode_nb')
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex05/display.html', {'movies': movies})


def remove(request):
    """127.0.0.1:8000/ex05/remove"""
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Movies.objects.filter(title=title).delete()

    movies = Movies.objects.all().order_by('episode_nb')
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex05/remove.html', {'movies': movies})
