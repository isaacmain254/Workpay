from django.urls import path, include 
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
    # login redirect
    path('', views.login_success, name='login-success'),
    path('edit/', views.edit, name='edit'),
    path('profile/<int:user_id>/', views.user_profile, name='profile'),
    path('edit-bio/<int:user_id>/', views.edit_bio, name='edit-bio'),
    path('add-project/', views.add_project, name='add-project'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit-project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete-project'),

    path('select-group/', views.select_group, name='select-group'),
]