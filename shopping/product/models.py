from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from accounts import models as m
import hashlib

class SearchData(models.Model):
    username = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    create_at = models.CharField(max_length=1000)
    def __str__(self):
        return self.person_name
 
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.IntegerField()
    discount = models.CharField(max_length=10)
    tag = models.CharField(max_length=20) # #어쩌고저쩌고
    genre = models.CharField(max_length=20) #가전 
    urls = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.product_name
    
@receiver(pre_save, sender=Product)
def generate_url(sender, instance, **kwargs):
    if not instance.urls:
        # Combine relevant fields to create a unique string for encryption
        url_code = f"{instance.product_name}-{instance.price}-{instance.tag}-{instance.genre}"
        
        # Hash the string using hashlib
        encr_url = hashlib.sha256(url_code.encode()).hexdigest()
        
        # Save the encrypted URL
        instance.urls = encr_url