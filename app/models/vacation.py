from django.db import models

class Vacation(models.Model):
    id = models.AutoField(primary_key= True)
    vid = models.IntegerField()
    vname= models.CharField(max_length=50)
    vamount= models.IntegerField()
