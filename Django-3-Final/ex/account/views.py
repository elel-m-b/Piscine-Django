import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


def account_page(request):
    """
    Renders the /account page. Its INITIAL appearance (login form vs.
    "Logged as ...") reflects whatever the server currently knows about
    the visitor's session - this is what makes a manual page refresh
    "return to the behaviour it had before refreshing", as required.
    Everything AFTER that first render is handled purely by AJAX/JS,
    without ever reloading the page.
    """
    return render(request, 'account/account.html', {
        'login_form': AuthenticationForm(),
    })


@require_POST
def ajax_login(request):
    """
    AJAX endpoint (POST only). Validates the given username/password with
    Django's own AuthenticationForm (free validation, as the subject's
    hint suggests) and logs the user in. Always answers with JSON so the
    frontend can update the page without a reload.
    """
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return JsonResponse({'success': True, 'username': user.username})

    return JsonResponse({'success': False, 'errors': form.errors}, status=400)


@require_POST
def ajax_logout(request):
    """AJAX endpoint (POST only) that logs the current user out."""
    logout(request)
    return JsonResponse({'success': True})
