from django.db import models
from datetime import datetime    
from django_mysql.models import ListCharField

GENDERS  = (
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            )

class userRegistration(models.Model):
    userId = models.CharField(max_length=50,default='',unique=True,blank=True)
    userName = models.CharField(max_length=50,default='',unique=True,blank=True)
    firstName = models.CharField(max_length=50,default='',blank=True)
    lastName = models.CharField(max_length=50,default='',blank=True)
    mobile = models.CharField(max_length=10,default='',blank=True)
    emailAddress = models.EmailField(max_length=50,default='',blank=True)
    password = models.CharField(max_length=100,default='',blank=True)
    profilePic = models.ImageField(upload_to='media',default='media/profile.jpeg')
    Groups = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100),blank=True
    )
    coverPic = models.ImageField(upload_to='media',default='media/cover.jpg')
    quote = models.CharField(max_length=1000,default='',blank=True)
    dOB = models.DateField(blank=True,null=True)
    gender = models.CharField(choices=GENDERS,max_length=1,blank=True)
    countryName = models.CharField(max_length=100,default='',blank=True)
    cityName = models.CharField(max_length=100,default='',blank=True)
    currentEducation = models.CharField(max_length=100,default='',blank=True)
    educationStartYear = models.CharField(max_length=10,default='',blank=True)
    educationEndYear = models.CharField(max_length=10,default='',blank=True)
    companyName = models.CharField(max_length=100,default='',blank=True)
    companyPosition = models.CharField(max_length=100,default='',blank=True)
    companyCity = models.CharField(max_length=50,default='',blank=True)
    companyDescription = models.CharField(max_length=1000,default='',blank=True)
    joinedDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Friend_Requests(models.Model):
    sender = models.CharField(max_length=50,default='')
    receiver = models.CharField(max_length=50,default='')
    senderName=models.CharField(max_length=75,default='')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.senderName

class AllFriends(models.Model):
    userId = models.CharField(max_length=50)
    Friends = ListCharField(
        base_field=models.CharField(max_length=50,blank=True),
        max_length=(100 * 100)
    )

    def __str__(self):
        return self.userId

class Notifications(models.Model):
    postId = models.CharField(max_length=50,blank=True,default='')
    notificationType = models.CharField(max_length=50,default='',blank=True)    # 'friend' for Friend Request 'like' for Like 'comment' for Comment and so on
    fullName = models.CharField(max_length=55, blank=True)
    sender = models.CharField(max_length=55, blank=True)
    receiver = models.CharField(max_length=55, blank=True)
    notification = models.CharField(max_length=100, blank=True)
    viewed = models.BooleanField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.fullName    

class UserPost(models.Model):
    postId = models.CharField(max_length=100,default='',unique=True) 
    userId = models.CharField(max_length=50,default='')
    userName = models.CharField(max_length=50,default='')
    post = models.FileField(upload_to="profiles",blank=True)
    Message = models.TextField(default="",blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    userPic = models.CharField(max_length=100,default='',blank=True)

class Story(models.Model):
    userId = models.CharField(max_length=50,default='')
    media = models.FileField(upload_to="profiles",blank=True)
    uploadTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.userId

class Album(models.Model):
    AlbumID = models.CharField(max_length=50,default='',blank=True,unique=True)
    Name = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Name

class Photos(models.Model):
    Album = models.CharField(max_length=50,default='',blank=True)
    PhotoID = models.CharField(max_length=50,default='',blank=True,unique=True)
    Image = models.ImageField(upload_to='media',blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Likes(models.Model):
    postId = models.CharField(max_length=100,default='',blank=True)
    postLikes = models.IntegerField(default=0,blank=True)
    postLikedBy = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    postLikedOf = models.CharField(max_length=50,default='',blank=True)

    def __str__(self):
        return self.postId

class Messages(models.Model):
    inboxId = models.CharField(max_length=50,default='',blank=True,unique=True)
    Users = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    MessageID = models.CharField(max_length=500,default='',blank=True,unique=True)
    sender = models.CharField(max_length=500,default='',blank=True)
    receiver = models.CharField(max_length=500,default='',blank=True)
    is_read = models.BooleanField(default=False,blank=True)
    Message = models.TextField(default='',blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.inboxId

class TempRoom(models.Model):
    RoomId = models.CharField(max_length=50,default='',blank=True,unique=True)
    Users = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )

    def __str__(self):
        return self.RoomId

class Groups(models.Model):
    groupId = models.CharField(max_length=50,default='',blank=True,unique=True)
    groupName = models.CharField(max_length=50,default='',blank=True)
    Members = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    groupInfo = models.CharField(max_length=50,default='',blank=True)
    groupPic = models.ImageField(upload_to='media',default='media/group.jpg',blank=True)
    def __str__(self):
        return self.groupName

class GroupChat(models.Model):
    groupId = models.CharField(max_length=50,default='',blank=True)
    messageID = models.CharField(max_length=50,default='',blank=True,unique=True)
    Message = models.TextField(default='',blank=True)
    sender = models.CharField(max_length=500,default='',blank=True)
    senderName = models.CharField(max_length=50,default='',blank=True)
    senderPic = models.CharField(max_length=50,default='',blank=True)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __list__(self):
        return self.Members

class Comments(models.Model):
    postId = models.CharField(max_length=100,default='',blank=True)
    commentId = models.CharField(max_length=100,default='',blank=True,unique=True)
    comment = models.TextField(default='',blank=True)
    commentedBy = models.CharField(max_length=500,default='',blank=True)
    commentedOf = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    userInfo = models.ForeignKey(userRegistration,on_delete=models.CASCADE)

    def __str__(self):
        return self.postId

class Replies(models.Model):
    postId = models.CharField(max_length=50,default='',blank=True)
    commentId = models.CharField(max_length=50,default='',blank=True)
    replyId = models.CharField(max_length=50,default='',blank=True)
    repliedBy = models.CharField(max_length=50,default='',blank=True)
    repliedOn = models.CharField(max_length=50,default='',blank=True)
    reply = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    userInfo = models.ForeignKey(userRegistration,on_delete=models.CASCADE)

    def __str__(self):
        return self.postId