from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        permissions = (
                ('manage_productcategories', 'Manage product categories'),)

    def get_absolute_url(self):
        return reverse('product-category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{}".format(self.name)

class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('product-type-list')

    def __str__(self):
        return "{}".format(self.name)

class UnitOfMeasurement(models.Model):
    unit = models.CharField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse('uom-list')

    def __str__(self):
        return "{}".format(self.unit)

class SellableItem(models.Model):
    name = models.CharField(max_length=100)
    internal_ref = models.CharField(max_length=100, default='', blank=True)
    item_type = models.ForeignKey(ProductType, default=0)
    category = models.ForeignKey(ProductCategory)
    description = RichTextField(blank=True, default='')

    def __str__(self):
        return "{}".format(self.name)

class Product(SellableItem):
    purchase_units_of_measurement = models.ManyToManyField(
            UnitOfMeasurement,
            through='PurchaseUnitOfMeasurement',
            through_fields=('product', 'unit_of_measurement'),
            related_name='purchase_units_of_measurement',
            blank=True)
    sale_units_of_measurement = models.ManyToManyField(
            UnitOfMeasurement,
            through='SaleUnitOfMeasurement',
            through_fields=('product', 'unit_of_measurement'),
            related_name='sale_units_of_measurement',
            blank=True)

    def get_absolute_url(self):
        return reverse('product-list')

    def __str__(self):
        return "{}".format(self.name)

class PurchaseUnitOfMeasurement(models.Model):
    product = models.ForeignKey(Product)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement)

    class Meta:
        unique_together = ('product', 'unit_of_measurement',)

class SaleUnitOfMeasurement(models.Model):
    product = models.ForeignKey(Product)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement)

    class Meta:
        unique_together = ('product', 'unit_of_measurement',)
