import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class CommentConsumer(WebsocketConsumer):
    def connect(self):
        print('CommentConsumer')
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
        postCommentedOf = text_data_json['postCommentedOf']
        postCommentedBy = text_data_json['postCommentedBy']
        loggedUser = text_data_json['loggedUser']
        comment = text_data_json['comment']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'postId' : postId,
                'postCommentedOf' : postCommentedOf,
                'postCommentedBy' : postCommentedBy,
                'loggedUser':loggedUser,
                'comment':comment,
             })

# Receive message from room group
    def chat_message(self, event):
        postId = event['postId']
        postCommentedOf = event['postCommentedOf']
        postCommentedBy = event['postCommentedBy']
        loggedUser = event['loggedUser']
        comment = event['comment']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'postId' : postId,
            'postCommentedOf' : postCommentedOf,
            'postCommentedBy' : postCommentedBy,
            'loggedUser':loggedUser,
            'comment':comment,
        }))

        