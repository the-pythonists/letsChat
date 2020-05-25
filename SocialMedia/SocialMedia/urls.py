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
    path('test/',views.test,name='test'),
    path('',views.index,name='index'),
    path("search/",views.search,name="search"),
    path('signup/',views.signup,name='signup'),
    path("uservalidate/", views.uservalidate,name="uservalidate"), #Check Username
    path('login/',views.login,name='login'),
    path("OtpGeneration/", views.OtpGeneration,name="OtpGeneration"),#Otp Generation
    path("story/",views.story,name="story"),
    path("storydelete/",views.storydelete,name="storydelete"),
    path("changepassword/",views.changepassword,name="changepassword"),
    path("PostSubmission/",views.PostSubmission,name="PostSubmission"),
    path("postlike/",views.postlike,name="postlike"),
    path("album/",views.album,name="album"),
    path("profile/",views.searchProfile,name="searchProfile"),
    path("profile/<str:user>/",views.profile,name="profile"),
    path("addfriend/",views.addfriend,name="addfriend"),
    path("requestConfirm/",views.requestConfirm,name="requestConfirm"),
    path("notifications/",views.notifications,name="notifications"),
    path("logout/",views.logout,name="logout"),
    path("userCoverInsert/",views.userCoverInsert,name="userCoverInsert"),#User Cover Pic Store
    path("friendSearch/", views.friendSearch,name="friendSearch"),#friend Search
    path("liveSearchProcess/",views.liveSearchProcess,name="liveSearchProcess"),#live Search Process
    path("incomingRequest/",views.incomingRequest,name="incomingRequest"),#incoming Request
    path("outgoingRequest/",views.outgoingRequest,name="outgoingRequest"),#incoming Request
    path("userIntroInsert/",views.userIntroInsert,name="userIntroInsert"),
    # path("Userprofile/",views.Userprofile,name="Userprofile"),#User Profile
    path("userProfileInsert/",views.userProfileInsert,name="userProfileInsert"),#User Profile Store
    path("myfriends/",views.myfriends,name="myfriends"), #User All Friends
    path("myFriendsProcess/",views.myFriendsProcess,name="myFriendsProcess"), #User All Friends Process
    path("automaticallylike/",views.automaticallylike,name="automaticallylike"), #Automatically Check the Like Count
    path("forgetPassword/",views.forgetPassword,name="forgetPassword"), #Forget Password
    path("forgetPasswordProcess/",views.forgetPasswordProcess,name="forgetPasswordProcess"), #Forget Password Process
    path("forgetPasswordOTP/",views.forgetPasswordOTP,name="forgetPasswordOTP"), #Forget Password OTP
    path("changeForgetPasword/",views.changeForgetPasword,name="changeForgetPasword"), #Forget change Forget Pasword Password OTP
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)