from django.db import models
import uuid

class AmadaaModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)

    class Meta:
        abstract = True
