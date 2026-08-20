from django.contrib.auth.forms import AuthenticationForm


def login_form(request):
    """
    Makes an (empty, unbound) login form available in every template's
    context, so the site-wide menu (Exercise 03) can embed it directly.

    When a login attempt fails, LoginView re-renders its template with a
    *bound* form (containing the errors) under the same context key
    ('form') -  that bound form takes priority over this one because the
    view's own context always overrides the context processors' context
    with the same key, so the errors still show up correctly in the menu.
    """
    return {'login_form': AuthenticationForm(request)}
