from django.db import models
from amadaa.models import AmadaaModel
from django.urls import reverse

# Create your models here.

class ProductCategory(AmadaaModel):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('product-category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{}".format(self.name)

class Product(AmadaaModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory)

    def __str__(self):
        return "%(self.name)s"
