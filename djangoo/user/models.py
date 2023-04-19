from email.policy import default
from django.db import models

class User_register(models.Model):
    Userid = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email= models.EmailField(max_length=255)
    Password= models.CharField(max_length=50)
    Confirmpassword = models.CharField(max_length=50)
    
class User_signin(models.Model):
    Username = models.CharField(max_length=255)
    Email= models.EmailField(max_length=255)