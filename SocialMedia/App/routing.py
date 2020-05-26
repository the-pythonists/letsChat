from django.urls import re_path

from . import consumers,notificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', notificationConsumer.ConfirmNotificationConsumer),
]