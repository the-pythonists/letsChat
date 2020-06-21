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
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path("OtpGeneration/", views.OtpGeneration,name="OtpGeneration"),#Otp Generation
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('test/',views.test,name='test'),
    path("search/",views.search,name="search"),
    path("uservalidate/", views.uservalidate,name="uservalidate"),

    path("imageStory/",views.imageStory,name="imageStory"),
    path("textStory/",views.textStory,name="textStory"),
    path("imageStorySubmissionForm/",views.imageStorySubmissionForm,name="imageStorySubmissionForm"),
    path("story/",views.story,name="story"),
    path("storySubmissionForm/",views.story,name="story"),
    path("storydelete/",views.storydelete,name="storydelete"),
    path("PostSubmission/",views.PostSubmission,name="PostSubmission"),

    path("postlike/",views.postlike,name="postlike"),
    path("postcomment/",views.postcomment,name="postcomment"),
    path("reply/",views.reply,name="reply"),
    
    path("reportGetPost/",views.reportGetPost,name="reportGetPost"),
    path("reportSubmission/",views.reportSubmission,name="reportSubmission"), #Report get from Deshboard
    
    path("taggedSearchFriends/",views.taggedSearchFriends,name="taggedSearchFriends"), #For Tagged Friends
   
    path('changepassword/',views.changepassword,name='changepassword'),
    path("forgetPassword/",views.forgetPassword,name="forgetPassword"), #Forget Password
    path("forgetPasswordOTP/",views.forgetPasswordOTP,name="forgetPasswordOTP"), #Forget Password
    path("forgetPasswordProcess/",views.forgetPasswordProcess,name="forgetPasswordProcess"), #Forget Password Process
    
    path("album/",views.album,name="album"),
    # path("createAlbumDetails/",views.createAlbumDetails,name="createAlbumDetails"), #For createAlbumDetails
    
    path("profile/",views.searchProfile,name="searchProfile"),
    path("profile/<str:user>/",views.profile,name="profile"),
    
    path("myfriends/",views.myfriends,name="myfriends"),
    path("myFriendsProcess/",views.myFriendsProcess,name="myFriendsProcess"), #User All Friends Process
    path("addfriend/",views.addfriend,name="addfriend"),
    path("requestConfirm/",views.requestConfirm,name="requestConfirm"),
    path("notifications/",views.notifications,name="notifications"),
    path("liveSearchProcess/",views.liveSearchProcess,name="liveSearchProcess"),#live Search Process
   
    path("userProfileInsert/",views.userProfileInsert,name="userProfileInsert"),#User Profile Store
    path("userIntroInsert/",views.userIntroInsert,name="userIntroInsert"),#Intro Insert
    path("userCoverInsert/",views.userCoverInsert,name="userCoverInsert"),#User Cover Pic Store
    path("friendSearch/", views.friendSearch,name="friendSearch"),#friend Search
    path("outgoingRequest/",views.outgoingRequest,name="outgoingRequest"),#incoming Request
    path("incomingRequest/",views.incomingRequest,name="incomingRequest"),#incoming Request
    # path("Userprofile/",views.Userprofile,name="Userprofile"),#User Profile
    
    path("messages/",views.messages,name="messages"),
    path("messages/<str:user>/",views.inbox,name="inbox"),
    path("groups/<str:group>/",views.groups,name="groups"),
    path("saveMessage/",views.saveMessage,name="saveMessage"),
    path("groupmessagesave/",views.groupMessage_Save,name="groupMessage_Save"),
    path("seenMessage/<str:sender>/<str:receiver>/",views.seenMessage,name="seenMessage"),
        
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)