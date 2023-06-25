from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class OrderManager(models.Manager):
    def create_order(self, user,product,stripe_invoice_id,quantity):
        order = self.create(user=user,product=product,stripe_invoice_id=stripe_invoice_id,quantity=quantity)
        # do something with the book
        return order

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stripe_invoice_id = models.TextField(default=None,blank=True, null=True)
    quantity = models.IntegerField()

    objects = OrderManager()

