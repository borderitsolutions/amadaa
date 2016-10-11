from django.db import models
from amadaa.models import AmadaaModel
from ckeditor.fields import RichTextField

# Create your models here.

class Contact(AmadaaModel):
    def __str__(self):
        try:
            return "{}, {}".format(self.person.last_name, 
                    self.person.first_name)
        except:
            return "{}".format(self.organization.name)

class Person(Contact):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Organization(Contact):
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

class PhoneType(AmadaaModel):
    phone_type = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.phone_type)

class PhoneNumber(AmadaaModel):
    contact = models.ForeignKey(Contact)
    phone_type = models.ForeignKey(PhoneType)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.phone_number)

class WebsiteType(AmadaaModel):
    website_type = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.website_type)

class Website(AmadaaModel):
    contact = models.ForeignKey(Contact)
    website_type = models.ForeignKey(WebsiteType)
    url = models.URLField()

    def __str__(self):
        return "{}".format(self.url)

