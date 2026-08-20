from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    """An article that can be written by any registered user and read
    by anyone (logged-in or not)."""

    title = models.CharField(max_length=64)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
    )
    created = models.DateTimeField(auto_now_add=True)
    synopsis = models.CharField(max_length=312)
    content = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.pk})


class UserFavouriteArticle(models.Model):
    """Links a user to one of their favourite articles."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favourites',
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='favourited_by',
    )

    class Meta:
        # A user cannot favourite the same article twice (Exercise 06).
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'article'], name='unique_user_favourite',
            )
        ]

    def __str__(self):
        return self.article.title
