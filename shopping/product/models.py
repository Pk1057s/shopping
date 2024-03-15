from django.db import models

class Tag(models.Model):
    person_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.person_name
 
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.IntegerField()
    discount = models.CharField(max_length=10)
    tag = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    def __str__(self):
        return self.product_name