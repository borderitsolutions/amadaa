from django.db import models
from django.urls import reverse
from contact.models import Organization
from product.models import Product

# Create your models here.

class Supplier(Organization):
    def get_absolute_url(self):
        return reverse('supplier-list')

    def __str__(self):
        return "{}".format(self.name)
