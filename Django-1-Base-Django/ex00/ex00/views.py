from django.shortcuts import render


def index(request):
    """Render the static Markdown Cheatsheet page."""
    context = {
        'title': 'Ex00: Markdown Cheatsheet',
    }
    return render(request, 'index.html', context)
