from django.db import models
from datetime import datetime    
from django_mysql.models import ListCharField

class userRegistration(models.Model):
    userId = models.CharField(max_length=50,default='')
    userName = models.CharField(max_length=50,default='')
    firstName = models.CharField(max_length=50,default='')
    lastName = models.CharField(max_length=50,default='')
    mobile = models.CharField(max_length=10,default='')
    emailAddress = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=100,default='')
    profilePic = models.ImageField(upload_to='media',default='media/profile.jpeg')
    coverPic = models.ImageField(upload_to='media',default='media/cover.jpg')   
    quote = models.CharField(max_length=1000,default='')
    dOB = models.CharField(max_length=20,default='')
    gender = models.CharField(max_length=10,default='')
    countryName = models.CharField(max_length=100,default='')
    cityName = models.CharField(max_length=100,default='')
    currentEducation = models.CharField(max_length=100,default='')
    educationStartYear = models.CharField(max_length=10,default='')
    educationEndYear = models.CharField(max_length=10,default='')
    companyName = models.CharField(max_length=100,default='')
    companyPosition = models.CharField(max_length=100,default='')
    companyCity = models.CharField(max_length=50,default='')
    companyDescription = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Friend_Requests(models.Model):
    senderId = models.CharField(max_length=50,default='')
    receiverId = models.CharField(max_length=50,default='')
    senderName=models.CharField(max_length=75,default='')

    def __str__(self):
        return self.senderName

class AllFriends(models.Model):
    userId = models.CharField(max_length=50)
    Friends = ListCharField(
        base_field=models.CharField(max_length=50),
        max_length=(100 * 100)
    )


    def __str__(self):
        return self.userId

class UserPost(models.Model):
    postId = models.CharField(max_length=100,default='') 
    userId = models.CharField(max_length=50,default='')
    post = models.ImageField(upload_to="profiles")
    Message = models.CharField(max_length=5000,default="")
    date = models.DateTimeField(default=datetime.now, blank=True)

class Likes(models.Model):
    postId = models.CharField(max_length=100)
    postLikes = models.IntegerField(default=0)
    postLikedBy = models.CharField(max_length=50,default='')
    postLikedOf = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.postId



# class AllFriends(models.Model):
#     FriendID = models.CharField(max_length=50,default='',blank=True,null=True)

#     def __str__(self):
#         return self.FriendID

# class FriendList(models.Model):
#     loggedUser = models.CharField(max_length=100,default='')
#     Friends = models.ManyToManyField(AllFriends,default='',blank=True,null=True)

#     def __str__(self):
#         return self.loggedUser