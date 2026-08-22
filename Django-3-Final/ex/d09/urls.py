from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('chat.urls')),
    # Convenience redirect, so visiting the bare domain lands somewhere useful.
    path('home/', RedirectView.as_view(pattern_name='chat:room_list'), name='home'),
]
