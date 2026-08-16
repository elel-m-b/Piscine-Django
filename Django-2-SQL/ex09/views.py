from django.http import HttpResponse
from django.shortcuts import render

from .models import People


def display(request):
    """127.0.0.1:8000/ex09/display"""
    people = (
        People.objects
        .filter(homeworld__climate__icontains='windy')
        .select_related('homeworld')
        .order_by('name')
    )

    if not people:
        message = (
            "No data available, please use the following command line before use: "
            "python3 manage.py loaddata ex09_initial_data.json"
        )
        return HttpResponse(message)

    return render(request, 'ex09/display.html', {'people': people})
