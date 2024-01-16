from django.db import models

# Create your models here.
class Users(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    GENDER_CHOICES = (('male', 'Male'),('female', 'Female'),('other', 'Other'))
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Mail = models.EmailField(unique=True)
    UserName = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)
    Profile_Picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

class Cart(models.Model):
    UserName = models.CharField(max_length=50)
    Prod_Name = models.CharField(max_length=50)
    Prod_Desc = models.CharField(max_length=50)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Total = models.IntegerField()