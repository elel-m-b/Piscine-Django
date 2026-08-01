"""WSGI config for helloworld_project project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld_project.settings')

application = get_wsgi_application()
