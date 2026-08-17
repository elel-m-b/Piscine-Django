from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import m2m_changed, post_delete
from django.dispatch import receiver

from .models import (
    DELETE_REPUTATION_THRESHOLD,
    DOWNVOTE_POINTS,
    DOWNVOTE_REPUTATION_THRESHOLD,
    UPVOTE_POINTS,
)


def recompute_reputation(user):
    """
    Recompute a user's reputation from scratch, based on all the
    upvotes/downvotes their (still existing) tips have received, then
    make sure their permissions match their new reputation.
    """
    if user is None or user.pk is None:
        return

    total = 0
    for tip in user.tips.all():
        total += tip.upvote_count * UPVOTE_POINTS
        total += tip.downvote_count * DOWNVOTE_POINTS

    user.reputation = total
    user.save(update_fields=['reputation'])
    sync_permissions(user)


def sync_permissions(user):
    """
    Grant or revoke the 'downvote_tip' and 'delete_tip' permissions
    depending on the user's current reputation.
    """
    from tips.models import Tip

    content_type = ContentType.objects.get_for_model(Tip)
    downvote_perm = Permission.objects.get(
        content_type=content_type, codename='downvote_tip',
    )
    delete_perm = Permission.objects.get(
        content_type=content_type, codename='delete_tip',
    )

    if user.reputation >= DOWNVOTE_REPUTATION_THRESHOLD:
        user.user_permissions.add(downvote_perm)
    else:
        user.user_permissions.remove(downvote_perm)

    if user.reputation >= DELETE_REPUTATION_THRESHOLD:
        user.user_permissions.add(delete_perm)
    else:
        user.user_permissions.remove(delete_perm)


@receiver(m2m_changed)
def on_vote_changed(sender, instance, action, **kwargs):
    """
    Runs whenever a Tip's `upvoters` or `downvoters` M2M field changes
    (a vote was added or removed). We only care about the field names
    used by the Tip model, so we check the sender's field name below.
    """
    if action not in ('post_add', 'post_remove', 'post_clear'):
        return

    # `instance` is a Tip only when the upvoters/downvoters field of a
    # Tip changed (as opposed to e.g. a User's permissions changing).
    from tips.models import Tip
    if isinstance(instance, Tip):
        recompute_reputation(instance.author)


@receiver(post_delete)
def on_tip_deleted(sender, instance, **kwargs):
    """
    When a Tip is deleted, the votes it had received should no longer
    influence its author's reputation.
    """
    from tips.models import Tip
    if sender is Tip:
        recompute_reputation(instance.author)
