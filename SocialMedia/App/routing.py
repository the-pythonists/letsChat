from django.urls import re_path

from . import consumers,likeConsumer

websocket_urlpatterns = [
    re_path(r'ws/like/(?P<room_name>\w+)/$', likeConsumer.likeConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]