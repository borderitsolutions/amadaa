from django.db import models

# Create your models here.

class Person(AmadaaModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Organization(AmadaaModel):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
            Person,
            through='Membership',
            through_fields=('organization', 'person'))

    def __str__(self):
        return "{}".format(self.name)

class Membership(AmadaaModel):
    organization = models.ForeignKey(Organization)
    person = models.ForeignKey(Person)

    def __str__(self):
        return "{} member of {}".format(self.person, self.organization)
