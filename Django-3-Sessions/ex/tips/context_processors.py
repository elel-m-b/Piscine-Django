import random
import time

from django.conf import settings


def anonymous_session(request):
    """
    Give every anonymous visitor a random display name that is picked
    from settings.RANDOM_NAMES and stays valid for
    settings.ANONYMOUS_NAME_VALIDITY seconds. Once that time has passed,
    a brand-new name is picked the next time a page is loaded.

    Because this runs on every single request (it's a context processor),
    the name is always fresh/consistent on every page - no manual reload
    trickery needed.
    """
    if request.user.is_authenticated:
        # Logged-in users use their real username, handled elsewhere.
        return {}

    now = time.time()
    name = request.session.get('anon_name')
    created_at = request.session.get('anon_name_created_at')

    name_expired = (
        name is None
        or created_at is None
        or (now - created_at) > settings.ANONYMOUS_NAME_VALIDITY
    )

    if name_expired:
        name = random.choice(settings.RANDOM_NAMES)
        request.session['anon_name'] = name
        request.session['anon_name_created_at'] = now

    return {'anon_name': name}
