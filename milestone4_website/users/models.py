from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    first_name = models.TextField(default=None,blank=True, null=True)
    last_name = models.TextField(default=None,blank=True, null=True)
    address_1 = models.TextField(default=None,blank=True, null=True)
    address_2 = models.TextField(default=None,blank=True, null=True)
    address_city = models.TextField(default=None,blank=True, null=True)
    address_country = models.TextField(default=None,blank=True, null=True)
    phone = models.TextField(default=None,blank=True, null=True)
    stripe_customer_id = models.TextField(default=None,blank=True, null=True)

    def __str__(self):
        return self.username
