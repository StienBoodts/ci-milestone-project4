from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    favourite = models.BooleanField(null=True)


    def __str__(self):
        return self.favourite
