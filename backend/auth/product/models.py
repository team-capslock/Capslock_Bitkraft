from django.db import models


from store.models import *
# Creatfre your models here.
class ProductDetail(models.Model):
    store = models.ForeignKey(StoreDetail,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    image_url = models.URLField(max_length=500,blank=True, null=True) # company logo here
    description = models.TextField(max_length=400,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    # category = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product'


class Hit(models.Model):
    store = models.ForeignKey(StoreDetail,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(ProductDetail,on_delete=models.CASCADE,null=True,blank=True)
    ip = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    postal_code = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hit'
