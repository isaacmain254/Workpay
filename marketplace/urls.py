from django.urls import path
from . import views

# app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.client_page, name='client'),
    path('jobs/', views.jobs_page, name='jobs'),
]