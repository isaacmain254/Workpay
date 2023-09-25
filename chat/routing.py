from django.urls import path, re_path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    path("chat/<uuid:thread_id>/", ChatConsumer.as_asgi()),
]