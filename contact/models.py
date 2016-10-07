from django.db import models

# Create your models here.

class Person(AmadaaModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
