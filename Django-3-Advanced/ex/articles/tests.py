"""
Exercise 06: automated tests checking the access-control rules of the
site. Run them with:

    python3 manage.py test articles
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Article, UserFavouriteArticle


class AccessControlTests(TestCase):
    """
    'favourites', 'publications' and 'publish' (views + templates) must
    only be reachable by a logged-in (registered) user.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='testpass123')
        self.article = Article.objects.create(
            title='A Test Article',
            author=self.user,
            synopsis='A short synopsis for testing purposes.',
            content='Some article content.',
        )

    def test_favourites_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse('articles:favourites'))
        self.assertRedirects(
            response,
            f"{reverse('articles:login')}?next={reverse('articles:favourites')}",
        )

    def test_favourites_accessible_to_logged_in_user(self):
        self.client.login(username='alice', password='testpass123')
        response = self.client.get(reverse('articles:favourites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/favourite_list.html')

    def test_publications_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse('articles:publications'))
        self.assertRedirects(
            response,
            f"{reverse('articles:login')}?next={reverse('articles:publications')}",
        )

    def test_publications_accessible_to_logged_in_user(self):
        self.client.login(username='alice', password='testpass123')
        response = self.client.get(reverse('articles:publications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/publication_list.html')

    def test_publish_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse('articles:publish'))
        self.assertRedirects(
            response,
            f"{reverse('articles:login')}?next={reverse('articles:publish')}",
        )

    def test_publish_accessible_to_logged_in_user(self):
        self.client.login(username='alice', password='testpass123')
        response = self.client.get(reverse('articles:publish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_publish.html')

    def test_publish_creates_article_with_logged_in_user_as_author(self):
        self.client.login(username='alice', password='testpass123')
        self.client.post(reverse('articles:publish'), {
            'title': 'Brand New Article',
            'synopsis': 'A synopsis.',
            'content': 'Some content.',
        })
        article = Article.objects.get(title='Brand New Article')
        self.assertEqual(article.author, self.user)


class RegisterAccessTests(TestCase):
    """A registered (logged-in) user cannot access the registration form."""

    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='testpass123')

    def test_logged_out_user_can_access_register_page(self):
        response = self.client.get(reverse('articles:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_logged_in_user_cannot_access_register_page(self):
        self.client.login(username='bob', password='testpass123')
        response = self.client.get(reverse('articles:register'))
        # 'home' itself immediately redirects to 'articles' (Exercise 00),
        # so we only assert the first hop lands on 'home'.
        self.assertRedirects(
            response, reverse('articles:home'), target_status_code=302,
        )


class FavouriteDuplicationTests(TestCase):
    """A user cannot add the same article to their favourites twice."""

    def setUp(self):
        self.user = User.objects.create_user(username='carol', password='testpass123')
        self.author = User.objects.create_user(username='dave', password='testpass123')
        self.article = Article.objects.create(
            title='Once Is Enough',
            author=self.author,
            synopsis='A synopsis.',
            content='Some content.',
        )
        self.client.login(username='carol', password='testpass123')

    def test_adding_the_same_article_twice_does_not_duplicate_it(self):
        url = reverse('articles:add_favourite', args=[self.article.pk])
        self.client.post(url)
        self.client.post(url)  # second, duplicate attempt
        count = UserFavouriteArticle.objects.filter(
            user=self.user, article=self.article,
        ).count()
        self.assertEqual(count, 1)

    def test_favourite_appears_exactly_once_in_favourites_list(self):
        url = reverse('articles:add_favourite', args=[self.article.pk])
        self.client.post(url)
        self.client.post(url)
        response = self.client.get(reverse('articles:favourites'))
        self.assertEqual(len(response.context['favourites']), 1)
