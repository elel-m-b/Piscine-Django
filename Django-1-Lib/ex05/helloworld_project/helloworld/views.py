from django.http import HttpResponse


def hello_world(request):
    """Return a simple 'Hello World!' text response."""
    return HttpResponse("Hello World!")
