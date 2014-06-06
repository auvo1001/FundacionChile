from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=128)

    def __unicode__(self):
         return self.name

class Organization(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=255)
    address1 = models.CharField( max_length=255)
    address2 = models.CharField( max_length=255, blank=True)
    city = models.CharField( max_length=128)
    state_province = models.CharField(max_length=128, blank=True)
    url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('org-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name

class Representative(models.Model):
    FName = models.CharField(max_length=255)
    LName = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    org = models.ForeignKey(Organization)

    def __unicode__(self):
        return '%s %s' % (self.FName, self.LName)

class Trip(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    org = models.ForeignKey(Organization)

    def __unicode__(self):
        return '%s %s' % (self.date, self.org)

class User(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

