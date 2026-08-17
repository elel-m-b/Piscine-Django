from django.conf import settings
from django.db import models


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tips',
    )
    date = models.DateTimeField(auto_now_add=True)

    # ManyToMany fields are used instead of simple counters so that we can
    # always know EXACTLY who voted, and easily toggle/switch a vote
    # without ever risking a wrong or negative count.
    upvoters = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='upvoted_tips',
        blank=True,
    )
    downvoters = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='downvoted_tips',
        blank=True,
    )

    class Meta:
        ordering = ['-date']
        permissions = [
            ('downvote_tip', 'Can downvote a tip'),
        ]

    def __str__(self):
        return f'{self.content[:40]} ({self.author})'

    @property
    def upvote_count(self):
        return self.upvoters.count()

    @property
    def downvote_count(self):
        return self.downvoters.count()
