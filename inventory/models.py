from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Location(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']
