from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getmovies/', views.getmovies, name='movies'),
    path('moviedetails/<int:id>', views.moviedetails, name='moviedetails'),
    path('newMovie/', views.newMovie, name='newmovie'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]