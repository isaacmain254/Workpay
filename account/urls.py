from django.urls import path, include 
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.user_profile, name='profile'),
]