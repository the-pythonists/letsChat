import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from App.models import userRegistration

class StatusConsumer(WebsocketConsumer):
    def connect(self):
        print('StatusConsumer')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        userRegistration.objects.filter(userId=userId).update(onlineStatus=False)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    def receive(self, text_data):
        global userId
        text_data_json = json.loads(text_data)
        userId = text_data_json['userId']
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'userId': userId,
             })

# Receive message from room group
    def chat_message(self, event):
        userId = event['userId']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'userId':userId,
        }))

        