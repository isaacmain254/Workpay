from django.urls import path, include 
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
    # login redirect
    path('', views.login_success, name='login-success'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.user_profile, name='profile'),

    path('select-group/', views.select_group, name='select-group'),
]