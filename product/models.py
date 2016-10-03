from django.db import models
from amadaa.models import AmadaaModel
from django.urls import reverse

# Create your models here.

class ProductCategory(AmadaaModel):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('product-category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{}".format(self.name)
