from django.db import models

# Create your models here.
class Product(models.Model):
   name  = models.TextField()
   stripe_id = models.TextField(default=None, blank=True, null=True)
   quantity = models.IntegerField()
    