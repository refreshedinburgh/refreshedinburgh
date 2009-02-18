import datetime

from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=60)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=10, decimal_places=8)
    link = models.URLField()


class Event(models.Model):
    location = models.ForeignKey(Location)
    dtstart = models.DateTimeField()
    copy = models.TextField()
    upcoming_link = models.URLField()
