from django.db import models
from main.models import  *
# Create your models here.
class StoreDetail(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(max_length=400,null=True,blank=True)
    logo = models.URLField(max_length=500,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    url = models.URLField(max_length=400,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    postal_code = models.CharField(max_length=100,null=True,blank=True)
    plugInstall = models.BooleanField(null=True,blank=True)
    api_key = models.CharField(max_length=200,null=True,blank=True)

    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = 'store_detail'

