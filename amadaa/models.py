from django.db import models
import uuid

class AmadaaModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True
