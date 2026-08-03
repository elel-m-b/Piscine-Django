from django.shortcuts import render


def django_page(request):
    context = {'page_title': 'Ex01: Django, Web Framework.'}
    return render(request, 'ex01/ex01-django.html', context)


def display_page(request):
    context = {'page_title': 'Ex01: Display Process of a Static Page.'}
    return render(request, 'ex01/ex01-display.html', context)


def templates_page(request):
    context = {'page_title': 'Ex01: Template Engine.'}
    return render(request, 'ex01/ex01-template.html', context)
