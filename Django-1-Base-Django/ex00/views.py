from django.shortcuts import render


def index(request):
    """Display the Markdown cheatsheet static page."""
    context = {
        'page_title': 'Ex00: Markdown Cheatsheet',
    }
    return render(request, 'ex00/index.html', context)
