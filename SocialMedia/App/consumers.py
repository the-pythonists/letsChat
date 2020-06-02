import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class RequestConsumer(WebsocketConsumer):
    def connect(self):
        print('helooooooooo')
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
        text_data_json = json.loads(text_data)
        print(text_data_json)
        action = text_data_json['action']
        if action == 'add':
            sender = text_data_json['sender']
            receiver = text_data_json['receiver']
            userFullName = text_data_json['userFullName']
            userPic = text_data_json['userPic']
        # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'action':'add',
                    'sender': sender,
                    'receiver':receiver,
                    'userFullName':userFullName,
                    'userPic':userPic
                })
        elif action == 'cancel':
            sender = text_data_json['sender']
            receiver = text_data_json['receiver']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'action':'cancel',
                    'sender': sender,
                    'receiver':receiver
                })
        elif action == 'confirm':
            sender = text_data_json['sender']
            receiver = text_data_json['receiver']
            name = text_data_json['name']
            userPic = text_data_json['userPic']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'action':'confirm',
                    'sender': sender,
                    'receiver':receiver,
                    'name':name,
                    'userPic':userPic
                })
        elif action == 'unfriend':
            sender = text_data_json['sender']
            receiver = text_data_json['receiver']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'action':'unfriend',
                    'sender': sender,
                    'receiver':receiver
                })



    # Receive message from room group
    def chat_message(self, event):
        action = event['action']
        if action == 'add':
            sender = event['sender']
            receiver = event['receiver']
            userFullName = event['userFullName']
            userPic = event['userPic']

        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'action':action,
                'sender': sender,
                'receiver':receiver,
                'userFullName':userFullName,
                'userPic':userPic
            }))

        elif action == 'cancel':
            sender = event['sender']
            receiver = event['receiver']

        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'action':action,
                'sender': sender,
                'receiver':receiver
            }))
        
        elif action == 'confirm':
            sender = event['sender']
            receiver = event['receiver']
            name = event['name']
            userPic = event['userPic']

        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'action':action,
                'sender': sender,
                'receiver':receiver,
                'name':name,
                'userPic':userPic
            }))
        elif action == 'unfriend':
            sender = event['sender']
            receiver = event['receiver']

        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'action':action,
                'sender': sender,
                'receiver':receiver
            }))


