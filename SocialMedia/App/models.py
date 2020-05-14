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
    quote = models.CharField(max_length=1000,default='',blank=True)
    dOB = models.CharField(max_length=20,default='',blank=True)
    gender = models.CharField(max_length=10,default='',blank=True)
    countryName = models.CharField(max_length=100,default='',blank=True)
    cityName = models.CharField(max_length=100,default='',blank=True)
    currentEducation = models.CharField(max_length=100,default='',blank=True)
    educationStartYear = models.CharField(max_length=10,default='',blank=True)
    educationEndYear = models.CharField(max_length=10,default='',blank=True)
    companyName = models.CharField(max_length=100,default='',blank=True)
    companyPosition = models.CharField(max_length=100,default='',blank=True)
    companyCity = models.CharField(max_length=50,default='',blank=True)
    companyDescription = models.CharField(max_length=1000,default='',blank=True)

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
    userName = models.CharField(max_length=50,default='')
    post = models.ImageField(upload_to="profiles",blank=True)
    Message = models.CharField(max_length=5000,default="",blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    userPic = models.CharField(max_length=50,default='',blank=True)

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
