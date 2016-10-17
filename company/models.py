from django.db import models
from django.contrib.auth.models import User
from contact.models import Organization

# Create your models here.

class Company(Organization):
    users = models.ManyToManyField(User)

    def __str__(self):
        return "{}".format(self.name)

class Branch(models.Model):
    company = models.ForeignKey(Company)
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)
