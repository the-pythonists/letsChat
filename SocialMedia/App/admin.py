from django.contrib import admin
from django.apps import apps

myapp = apps.get_app_config('App')
for model in myapp.get_models():
    admin.site.register(model)

# admin.site.register(userRegistration)
# admin.site.register(Friend_Requests)
# admin.site.register(UserPost)
# admin.site.register(Likes)
# admin.site.register(AllFriends)
# admin.site.register(Notifications)
# admin.site.register(Story)
# admin.site.register(Album)
# admin.site.register(Photos)
# admin.site.register(Messages)
# admin.site.register(TempRoom)
# admin.site.register(Comments)