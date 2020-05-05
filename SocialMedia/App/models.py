from django.db import models

class userRegistration(models.Model):
    userId = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    emailAddress = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName + ' ' + self.lastName