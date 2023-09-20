import json 
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

user = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('connected')
    
    def disconnect(self, close_code):
        print('disconnected')

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({'message': message}))