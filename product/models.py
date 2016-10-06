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

class ProductType(AmadaaModel):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('product-type-list')

    def __str__(self):
        return "{}".format(self.name)

class UnitOfMeasurement(AmadaaModel):
    unit = models.CharField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse('uom-list')

    def __str__(self):
        return "%(self.unit)s"

class Product(AmadaaModel):
    name = models.CharField(max_length=100)
    internal_ref = models.CharField(max_length=100, default='')
    category = models.ForeignKey(ProductCategory)
    description = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('product-list')

    def __str__(self):
        return "%(self.name)s"
