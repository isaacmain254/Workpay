import json 
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import ChatMessage, Thread


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        self.room_name = self.scope["url_route"]["kwargs"]["thread_id"]
        print(self.room_name)
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print('disconnected')
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        print('received', text_data)
        data = json.loads(text_data)
        message = data["message"]
        sender_id = data['sender_id']


        # save message to the database
        await self.save_message(message)
      
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender_id": sender_id,
                

            }
        )

    async def chat_message(self, event):
        print('chat message', event)
        message = event["message"]
        sender_id = event['sender_id']
        

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "sender_id": sender_id,
            
        }))
    
    # save the message to the database
    @database_sync_to_async
    def save_message(self, message):
        thread = Thread.objects.get(id=self.room_name)
       
        sent_by = self.scope['user']
        new_message = ChatMessage.objects.create(message=message, sent_by=sent_by, thread=thread )
        return new_message