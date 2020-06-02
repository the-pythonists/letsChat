import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ConfirmNotificationConsumer(WebsocketConsumer):
    def connect(self):
        print('req conf')
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
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        name = text_data_json['name']
        senderPic = text_data_json['senderPic']

# Receive message from room group
    def chat_message(self, event):
        action = event['action']
        sender = event['sender']
        receiver = event['receiver']
        name = event['name']
        senderPic = event['senderPic']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'action':action,
            'sender': sender,
            'receiver':receiver,
            'name':name,
            'senderPic':senderPic
        }))

        