from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    address_1 = models.TextField()
    address_2 = models.TextField()
    address_city = models.TextField()
    address_country = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
