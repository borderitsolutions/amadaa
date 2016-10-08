from django.db import models
from contact.models import Organization
from product.models import Product

# Create your models here.

class Supplier(Organization):
    products = models.ManyToManyField(Product)

    def __str__(self):
        return "{}".format(self.name)
