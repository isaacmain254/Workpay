from django.urls import path
from . import views

# app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('freelancers/', views.client_page, name='freelancers'),
    path('jobs/', views.jobs_page, name='jobs'),
]