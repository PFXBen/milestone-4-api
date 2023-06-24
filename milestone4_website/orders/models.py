from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stripe_invoice_id = models.TextField(default=None,blank=True)
    quantity = models.IntegerField()
