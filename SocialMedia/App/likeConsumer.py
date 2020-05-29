import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class likeConsumer(WebsocketConsumer):
    def connect(self):
        print('LikeConsumer')
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
        postId = text_data_json['postId']
        postLikedOf = text_data_json['postLikedOf']
        postLikedBy = text_data_json['postLikedBy']
        loggedUser = text_data_json['loggedUser']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'postId': postId,
                'postLikedOf':postLikedOf,
                'postLikedBy':postLikedBy,
                'loggedUser':loggedUser
             })

# Receive message from room group
    def chat_message(self, event):
        postId = event['postId']
        postLikedOf = event['postLikedOf']
        postLikedBy = event['postLikedBy']
        loggedUser = event['loggedUser']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'postId':postId,
            'postLikedOf': postLikedOf,
            'postLikedBy':postLikedBy,
            'loggedUser':loggedUser
        }))

        