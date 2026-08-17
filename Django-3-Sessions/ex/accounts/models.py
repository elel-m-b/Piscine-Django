from django.contrib.auth.models import AbstractUser
from django.db import models

# Reputation thresholds that unlock extra permissions.
DOWNVOTE_REPUTATION_THRESHOLD = 15
DELETE_REPUTATION_THRESHOLD = 30

# Reputation points awarded/removed per vote.
UPVOTE_POINTS = 5
DOWNVOTE_POINTS = -2


class User(AbstractUser):
    """
    Our own User class (replacing django.contrib.auth.models.User) so we
    can attach a `reputation` score to every account. The reputation
    automatically unlocks the "downvote_tip" and "delete_tip" permissions
    once it crosses certain thresholds (see accounts/signals.py).
    """
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username} ({self.reputation})'
