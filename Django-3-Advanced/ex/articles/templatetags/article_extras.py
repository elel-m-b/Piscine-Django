from django import template
from django.utils.translation import ngettext

register = template.Library()


@register.filter(name='short_synopsis')
def short_synopsis(value, length=20):
    """
    Custom filter (Exercise 03): shortens a synopsis to at most `length`
    characters, replacing anything cut off with a single ellipsis '...'.

    Usage in a template: {{ article.synopsis|short_synopsis:20 }}
    """
    if value is None:
        return ''
    value = str(value)
    length = int(length)
    if len(value) <= length:
        return value
    return value[:length].rstrip() + '\u2026'


@register.filter(name='days_since')
def days_since(value):
    """
    Custom filter (Exercise 03): the "published for" column - how long
    ago (in whole days) an article was published.

    Usage: {{ article.created|days_since }}
    """
    from django.utils import timezone
    if value is None:
        return ''
    delta = timezone.now() - value
    days = delta.days
    if days <= 0:
        return 'today'
    return ngettext('%(count)d day', '%(count)d days', days) % {'count': days}
