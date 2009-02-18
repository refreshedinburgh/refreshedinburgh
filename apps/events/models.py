import datetime

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    street = models.CharField(max_length=128, blank=True)
    post_code = models.CharField(max_length=8, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True,
        null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8,
        blank=True, null=True)
    url = models.URLField('URL', blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique_for_year=True)
    date = models.DateTimeField(unique=True)
    location = models.ForeignKey(Location)
    copy = models.TextField()
    upcoming_link = models.URLField(blank=True)

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)

    def __unicode__(self):
        return self.title
