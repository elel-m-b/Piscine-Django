"""
URL configuration for hellenica project.

Every "real" page of the site lives under a language-code prefix
(e.g. /en/articles, /fr/articles) thanks to i18n_patterns, as required by
Exercise 05. The admin site and the language switcher itself stay outside
that prefix.
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Lets <form action="{% url 'set_language' %}"> switch the active
    # language (used by the language-switcher link in the menu).
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('articles.urls')),
)
