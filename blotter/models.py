from django.contrib.gis.db import models
from django.contrib.localflavor.us.models import USStateField
from django.conf import settings
from geopy import geocoders

COLOR_CHOICES = (
    (1,    'blue'),
    (2,     'red'),
    (3,   'green'),
    (4,    'teal'),
    (5,  'yellow'),
    (6,  'purple'),
    (7, 'magenta'),
    (8,  'orange'),
    (9,   'black'),
)


class CrimeType(models.Model):
    type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    # marker_color shouldn't be a char field.
    marker_color = models.IntegerField(choices=COLOR_CHOICES, default=9, max_length=10)

    def __unicode__(self):
        return self.type

class Agency(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __unicode__(self):
        return self.name

class CrimeManager(models.Manager):

    def approved(self):
        return super(CrimeManager, self).get_query_set().filter(approved=True)

    def unapproved(self):
        return super(CrimeManager, self).get_query_set().filter(approved=False)


class Crime(models.Model):
    block = models.IntegerField()
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = USStateField(default="SC")
    agency = models.ForeignKey(Agency)
    date = models.DateField()
    crime_type = models.ForeignKey(CrimeType)
    description = models.TextField()
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    approved = models.BooleanField(default=False)

    objects = CrimeManager()

    @models.permalink
    def get_absolute_url(self):
        return ('crime-instance', 
            [int(self.date.year),
            self.date.strftime('%b'),
            int(self.date.day),
            self.id]
        )

    def get_coords(self):
        y = geocoders.Yahoo(settings.YAHOO_API_KEY)
        place, (lat, long) = y.geocode("%d %s in %s, %s" % (self.block, self.street, self.city, self.state))
        return (lat, long)

    def save(self):
        if self.latitude == None and self.longitude == None:
            self.latitude, self.longitude = self.get_coords()
        super(Crime, self).save()


    def __unicode__(self):
        return "%s at %d block of %s" % (self.crime_type, self.block, self.street)
