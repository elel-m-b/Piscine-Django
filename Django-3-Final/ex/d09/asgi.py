"""
ASGI config for d09 project.

This is what makes the project able to speak BOTH regular HTTP (normal
Django pages/AJAX) AND WebSockets (the live chat) at the same time:
ProtocolTypeRouter looks at the incoming connection type and sends it to
the right handler.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd09.settings')

# Must be created BEFORE importing anything that touches models, so that
# Django's app registry is ready.
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack  # noqa: E402
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402

import chat.routing  # noqa: E402

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})
