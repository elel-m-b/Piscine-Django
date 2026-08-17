from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, RegistrationForm, TipForm
from .models import Tip

User = get_user_model()


def home(request):
    tips = Tip.objects.select_related('author').all()

    form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                return redirect('tips:home')
        else:
            form = TipForm()

    return render(request, 'tips/home.html', {'tips': tips, 'form': form})


def register(request):
    # A logged-in user is not allowed to view the registration page.
    if request.user.is_authenticated:
        return redirect('tips:home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            user.is_active = True
            user.save()
            auth_login(request, user)
            return redirect('tips:home')
    else:
        form = RegistrationForm()

    return render(request, 'tips/register.html', {'form': form})


def login_view(request):
    # A logged-in user is not allowed to view the login page.
    if request.user.is_authenticated:
        return redirect('tips:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.cleaned_data['user'])
            return redirect('tips:home')
    else:
        form = LoginForm()

    return render(request, 'tips/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('tips:home')


@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if tip.upvoters.filter(id=request.user.id).exists():
        # Clicking upvote a 2nd time cancels the upvote.
        tip.upvoters.remove(request.user)
    else:
        tip.upvoters.add(request.user)
        # A tip cannot be both upvoted and downvoted by the same user.
        tip.downvoters.remove(request.user)
    return redirect('tips:home')


@login_required
def downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    # Downvoting is reserved to users with the "downvote_tip" permission,
    # except a tip's own author can always downvote their own tip.
    allowed = tip.author == request.user or request.user.has_perm('tips.downvote_tip')
    if not allowed:
        return redirect('tips:home')

    if tip.downvoters.filter(id=request.user.id).exists():
        tip.downvoters.remove(request.user)
    else:
        tip.downvoters.add(request.user)
        tip.upvoters.remove(request.user)
    return redirect('tips:home')


@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    # Only the tip's author, or a user with the "delete_tip" permission,
    # is allowed to delete it.
    if tip.author == request.user or request.user.has_perm('tips.delete_tip'):
        tip.delete()
    return redirect('tips:home')
