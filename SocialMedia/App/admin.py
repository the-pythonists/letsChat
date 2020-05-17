from django.contrib import admin
from .models import userRegistration,Friend_Requests,UserPost,Likes,AllFriends,Notifications,Story

admin.site.register(userRegistration)
admin.site.register(Friend_Requests)
admin.site.register(UserPost)
admin.site.register(Likes)
admin.site.register(AllFriends)
admin.site.register(Notifications)
admin.site.register(Story)