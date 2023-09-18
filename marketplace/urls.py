from django.urls import path
from . import views

# app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('freelancers/', views.client_page, name='freelancers'),
    path('jobs/', views.jobs_page, name='jobs'),
    path('post-job/', views.post_job, name='post-job'),
    # path('send_email/', views.sendEmail, name='send_email'),
    path('email-success/', views.email_success, name='email-success'),
]