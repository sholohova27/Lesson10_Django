from django.urls import path
from . import views

app_name = "quotes_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('quotes/', views.quotes, name='quotes'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
