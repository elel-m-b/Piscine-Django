from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from .forms import AddFavouriteForm, ArticleForm, RegisterForm
from .models import Article, UserFavouriteArticle


# ---------------------------------------------------------------------
# Exercise 00
# ---------------------------------------------------------------------

class HomeView(RedirectView):
    """Mandatory '/' URL: simply redirects to the Articles page."""
    pattern_name = 'articles:articles'


class ArticleListView(ListView):
    """Displays every recorded article, newest first (Exercise 03)."""
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


class LoginView(AuthLoginView):
    """
    Logs a logged-out user in. On success -> redirected to Home (via
    LOGIN_REDIRECT_URL). On failure -> the page (which extends base.html)
    is re-rendered with the errors, which also makes them appear in the
    site-wide menu embedded on every page (Exercise 03).
    """
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Exposed under the same key the menu expects, so a failed
        # attempt's error messages show up there too.
        context['login_form'] = context['form']
        return context


class LogoutView(AuthLogoutView):
    """Logs the current user out, then redirects to Home."""
    next_page = 'articles:home'


# ---------------------------------------------------------------------
# Exercise 01
# ---------------------------------------------------------------------

class PublicationListView(LoginRequiredMixin, ListView):
    """Every article written by the CURRENTLY logged-in user."""
    model = Article
    template_name = 'articles/publication_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDetailView(DetailView):
    """Every field of a single article, identified by its pk in the URL."""
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class FavouriteListView(LoginRequiredMixin, ListView):
    """The titles of the current user's favourite articles, as links."""
    model = UserFavouriteArticle
    template_name = 'articles/favourite_list.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(
            user=self.request.user
        ).select_related('article')


# ---------------------------------------------------------------------
# Exercise 02
# ---------------------------------------------------------------------

class RegisterView(UserPassesTestMixin, CreateView):
    """
    Lets a LOGGED-OUT visitor create a new account. A logged-in user must
    not be able to reach this page (Exercise 06 tests this) - they are
    simply redirected to Home instead.
    """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('articles:login')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        from django.shortcuts import redirect
        messages.info(self.request, _('You are already logged in.'))
        return redirect('articles:home')

    def form_valid(self, form):
        messages.success(self.request, _('Account created, you can now log in.'))
        return super().form_valid(form)


class ArticlePublishView(LoginRequiredMixin, CreateView):
    """
    Lets a logged-in user publish a new article. The 'author' field is
    never shown to the user - it's filled in here, during validation,
    with the currently logged-in user.
    """
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_publish.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddFavouriteView(LoginRequiredMixin, CreateView):
    """
    A field-less form (posted from the article Detail page) that adds the
    given article to the logged-in user's favourites. Both 'article' and
    'user' are filled in here, not typed by the visitor.
    """
    model = UserFavouriteArticle
    form_class = AddFavouriteForm

    def form_valid(self, form):
        article = Article.objects.get(pk=self.kwargs['pk'])
        # A user cannot favourite the same article twice (Exercise 06):
        # re-clicking the button is harmless, it just won't duplicate it.
        favourite, created = UserFavouriteArticle.objects.get_or_create(
            user=self.request.user, article=article,
        )
        self.object = favourite
        if created:
            messages.success(self.request, _('Added to your favourites.'))
        else:
            messages.info(self.request, _('This article is already in your favourites.'))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.article.get_absolute_url()
