from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/favourite/', views.AddFavouriteView.as_view(), name='add_favourite'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('publications/', views.PublicationListView.as_view(), name='publications'),
    path('publish/', views.ArticlePublishView.as_view(), name='publish'),
    path('favourites/', views.FavouriteListView.as_view(), name='favourites'),
]
