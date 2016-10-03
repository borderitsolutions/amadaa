from django.db import models
from amadaa.models import AmadaaModel
from django.urls import reverse

# Create your models here.

class ProductCategory(AmadaaModel):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

