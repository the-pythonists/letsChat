from django.contrib import admin
from .models import userRegistration,Friend_Requests,UserPost,Likes,AllFriends,Notifications,Story,Album,Photos,Messages,TempRoom

admin.site.register(userRegistration)
admin.site.register(Friend_Requests)
admin.site.register(UserPost)
admin.site.register(Likes)
admin.site.register(AllFriends)
admin.site.register(Notifications)
admin.site.register(Story)
admin.site.register(Album)
admin.site.register(Photos)
admin.site.register(Messages)
admin.site.register(TempRoom)
