from django.contrib.gis.db import models
from django.contrib.localflavor.us.models import USStateField
from django.conf import settings
from geopy import geocoders

COLOR_CHOICES = (
    ('blue',    'blue'),
    ('red',     'red'),
    ('green',   'green'),
    ('teal',    'teal'),
    ('yellow',  'yellow'),
    ('purple',  'purple'),
    ('magenta', 'magenta'),
    ('orange',  'orange'),
    ('black',   'black'),
)

class CrimeType(models.Model):
    type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    marker_color = models.CharField(choices=COLOR_CHOICES, default=9, max_length=1)

    def __unicode__(self):
        return self.type

class Agency(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __unicode__(self):
        return self.name

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

    @models.permalink
    def get_absolute_url(self):
        return ('crime-instance', 
            [int(self.date.year),
            self.date.strftime('%b'),
            int(self.date.day),
            self.id]
        )

    def save(self):
        if self.latitude == None and self.longitude == None:
            y = geocoders.Yahoo(settings.YAHOO_API_KEY)
            place, (lat, long) = y.geocode("%d %s in %s, %s" % (self.block, self.street, self.city, self.state))
            self.latitude = lat
            self.longitude = long
        super(Crime, self).save()


    def __unicode__(self):
        return "%s at %d block of %s" % (self.crime_type, self.block, self.street)
