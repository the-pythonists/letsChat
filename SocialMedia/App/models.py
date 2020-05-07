from django.db import models
from datetime import datetime    

class userRegistration(models.Model):
    userId = models.CharField(max_length=50,default='')
    firstName = models.CharField(max_length=50,default='')
    lastName = models.CharField(max_length=50,default='')
    mobile = models.CharField(max_length=10,default='')
    emailAddress = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=100,default='')
    profilePic = models.ImageField(upload_to='media',default='media/profile.jpeg')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Friend_Requests(models.Model):
    senderId = models.CharField(max_length=50,default='')
    receiverId = models.CharField(max_length=50,default='')
    senderName=models.CharField(max_length=75,default='')

    def __str__(self):
        return self.senderName

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