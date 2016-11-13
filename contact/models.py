from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Contact(models.Model):
    def __str__(self):
        try:
            return "{}, {}".format(self.person.last_name, 
                    self.person.first_name)
        except:
            return "{}".format(self.organization.name)

class Person(Contact):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('person-list')
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Organization(Contact):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
            Person,
            through='Membership',
            through_fields=('organization', 'person'))

    def get_absolute_url(self):
        return reverse('organization-list')

    def __str__(self):
        return "{}".format(self.name)

class Membership(models.Model):
    organization = models.ForeignKey(Organization)
    person = models.ForeignKey(Person)

    def __str__(self):
        return "{} member of {}".format(self.person, self.organization)

class PhoneType(models.Model):
    phone_type = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.phone_type)

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact)
    phone_type = models.ForeignKey(PhoneType)
    phone_number = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('phonenumber-list')

    def __str__(self):
        return "{}".format(self.phone_number)

class WebsiteType(models.Model):
    website_type = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.website_type)

class Website(models.Model):
    contact = models.ForeignKey(Contact)
    website_type = models.ForeignKey(WebsiteType)
    url = models.URLField()

    def __str__(self):
        return "{}".format(self.url)

