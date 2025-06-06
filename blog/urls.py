from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signUp_view, name='sign_up'),
    path('profile/', views.profile_view, name='profile'),
    path('index2/', views.index2, name='index2'),
]