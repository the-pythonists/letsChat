from django.db import models

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
