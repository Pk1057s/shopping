from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     
    ROLES = (
        ('admin', '관리자'),
        ('seller', '판매자'),
        ('vip', 'vip'),
        ('customer', '소비자')
    )
    role = models.CharField(max_length=10, choices=ROLES, default='customer')
    person_name = models.CharField(max_length=20, blank=False, null=True, verbose_name='이름')
    phone_number = models.CharField(max_length=15, blank=False, null=True, verbose_name='전화번호')
    address = models.CharField(max_length=100, blank=False, null=True, verbose_name='주소')

    class Meta:
        db_table = 'users'
