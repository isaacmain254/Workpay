from django.urls import path
from . import views

# app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_page),
    path('freelancer/', views.freelancer_page),
]