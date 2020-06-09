"""SocialMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('test/',views.test,name='test'),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name='index'),
    path("search/",views.search,name="search"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path("uservalidate/", views.uservalidate,name="uservalidate"),
    path("OtpGeneration/", views.OtpGeneration,name="OtpGeneration"),#Otp Generation
    path("story/",views.story,name="story"),
    path("storydelete/",views.storydelete,name="storydelete"),
    path("PostSubmission/",views.PostSubmission,name="PostSubmission"),
    path("postlike/",views.postlike,name="postlike"),
    path("postcomment/",views.postcomment,name="postcomment"),
    # path("automaticallylike/",views.automaticallylike,name="automaticallylike"), #Automatically Check the Like Count
    path("album/",views.album,name="album"),
    path("profile/",views.searchProfile,name="searchProfile"),
    path("profile/<str:user>/",views.profile,name="profile"),
    path("myfriends/",views.myfriends,name="myfriends"),
    path("myFriendsProcess/",views.myFriendsProcess,name="myFriendsProcess"), #User All Friends Process
    path("addfriend/",views.addfriend,name="addfriend"),
    path("requestConfirm/",views.requestConfirm,name="requestConfirm"),
    path("notifications/",views.notifications,name="notifications"),
    path("userCoverInsert/",views.userCoverInsert,name="userCoverInsert"),#User Cover Pic Store
    path("friendSearch/", views.friendSearch,name="friendSearch"),#friend Search
    path("liveSearchProcess/",views.liveSearchProcess,name="liveSearchProcess"),#live Search Process
    path("incomingRequest/",views.incomingRequest,name="incomingRequest"),#incoming Request
    path("outgoingRequest/",views.outgoingRequest,name="outgoingRequest"),#incoming Request
    # path("Userprofile/",views.Userprofile,name="Userprofile"),#User Profile
    path("userProfileInsert/",views.userProfileInsert,name="userProfileInsert"),#User Profile Store
    path("userIntroInsert/",views.userIntroInsert,name="userIntroInsert"),#Intro Insert
    path("messages/",views.messages,name="messages"),
    path("saveMessage/",views.saveMessage,name="saveMessage"),
    path("groupmessagesave/",views.groupMessage_Save,name="groupMessage_Save"),
    path("messages/<str:user>/",views.inbox,name="inbox"),
    path("groups/<str:group>/",views.groups,name="groups"),
        
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)