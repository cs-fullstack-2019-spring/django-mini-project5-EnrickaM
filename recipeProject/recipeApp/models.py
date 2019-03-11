from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreateNewUserModel(models.Model):
    first_name=models.CharField(max_length=200,default="")
    last_name=models.CharField(max_length=200,default='')
    email=models.EmailField(max_length=200,default='')
    username=models.CharField(max_length=200,default='')
    password=models.CharField(max_length=20,default='')
    confirm_password=models.CharField(max_length=20,default='')
    foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return "This new user is: " + str(self.username)



class NewrecipeModel(models.Model):
    name=models.CharField(max_length=200,default='')
    maker=models.CharField(max_length=200,default='')
    datecreated=models.DateField(default=None)
    description=models.CharField(max_length=200,default='')


