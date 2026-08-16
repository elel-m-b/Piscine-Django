from django.shortcuts import render

from .models import People


def search(request):
    """127.0.0.1:8000/ex10"""
    genders = (
        People.objects
        .exclude(gender__isnull=True)
        .exclude(gender__exact='')
        .order_by('gender')
        .values_list('gender', flat=True)
        .distinct()
    )

    results = None
    searched = False

    if request.method == 'POST':
        searched = True
        min_date = request.POST.get('min_date') or None
        max_date = request.POST.get('max_date') or None
        diameter_gt = request.POST.get('diameter_gt') or None
        gender = request.POST.get('gender') or None

        results = []
        try:
            people_qs = People.objects.select_related('homeworld').filter(gender=gender)
            if diameter_gt not in (None, ''):
                people_qs = people_qs.filter(homeworld__diameter__gte=diameter_gt)
            else:
                people_qs = people_qs.filter(homeworld__isnull=False)

            for person in people_qs:
                movies_qs = person.movies.all()
                if min_date:
                    movies_qs = movies_qs.filter(release_date__gte=min_date)
                if max_date:
                    movies_qs = movies_qs.filter(release_date__lte=max_date)

                for movie in movies_qs:
                    results.append({
                        'movie_title': movie.title,
                        'name': person.name,
                        'gender': person.gender,
                        'homeworld': person.homeworld.name if person.homeworld else '',
                        'diameter': person.homeworld.diameter if person.homeworld else '',
                    })

            results.sort(key=lambda r: (r['movie_title'], r['name']))
        except Exception:
            results = []

    context = {
        'genders': genders,
        'results': results,
        'searched': searched,
    }
    return render(request, 'ex10/search.html', context)
