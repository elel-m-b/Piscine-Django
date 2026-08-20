from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article, UserFavouriteArticle


class RegisterForm(UserCreationForm):
    """
    Django already ships a ready-made form for creating users with a
    username, a password and a password-confirmation field:
    UserCreationForm. We simply reuse it (Exercise 02 hints at this!)
    instead of re-inventing the wheel.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)


class ArticleForm(forms.ModelForm):
    """
    Used by the 'Publish' CreateView. The 'author' field is intentionally
    left out: the view fills it in automatically from the logged-in user
    during validation (see ArticlePublishView.form_valid).
    """

    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']


class AddFavouriteForm(forms.ModelForm):
    """
    Used by the 'Add to favourite' CreateView. No field is visible to the
    user: both 'article' and 'user' are filled in by the view itself
    (from the URL and from the logged-in user), never typed by hand.
    """

    class Meta:
        model = UserFavouriteArticle
        fields = []
