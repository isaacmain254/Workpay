from django.urls import path
from . import views

urlpatterns = [
    # messages room without id
    path('', views.messages, name='messages'),
    # messages page with room_id parameter
    path('<uuid:thread_id>/', views.messages, name='thread-with-messages'),
    # Add a URL pattern to create or open a thread/room
    path('create_or_open_thread/<int:user_id>/', views.create_or_open_thread, name='create_or_open_thread'),
]