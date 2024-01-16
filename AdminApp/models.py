from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your models here.
class Category(models.Model):
    Cat_Name = models.CharField(max_length=50, null="true", blank="true")
    Cat_Desc = models.CharField(max_length=50, null="true", blank="true")
    Cat_Image = models.ImageField(upload_to="Cat_Images", null="true", blank="true")

class Products(models.Model):
    Cat_Name = models.CharField(max_length=50, null="true", blank="true")
    Prod_Name = models.CharField(max_length=50, null="true", blank="true")
    Prod_Desc = models.CharField(max_length=50, null="true", blank="true")
    Price = models.IntegerField(null="true",blank="true")
    Prod_Image = models.ImageField(upload_to="Product_Images", null="true", blank="true")
