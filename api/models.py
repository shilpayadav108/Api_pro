from django.db import models

# Create your models here.
class Shopper(models.Model):
    
    
    action = models.CharField(max_length=50,null=True,blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    publisher_id = models.CharField(max_length=50,null=True,blank=True)    
    
    shopper_id = models.CharField(max_length=250,null=True,blank=True)
    
    