from django.contrib import admin
from .models import userRegistration,Friend_Requests,UserPost,Likes

admin.site.register(userRegistration)
admin.site.register(Friend_Requests)
admin.site.register(UserPost)
admin.site.register(Likes)