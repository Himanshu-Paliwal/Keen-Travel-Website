from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    contact= models.IntegerField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    repassword = models.CharField(max_length=50)
