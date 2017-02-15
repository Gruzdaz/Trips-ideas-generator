from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=75)
    category_choices = (
        ('history', 'History'),
        ('nature', 'Nature'),
        ('architecture', 'Architecture'),
        ('entertainment', 'Entertainment'),

    )
    category = models.CharField(
        max_length= 13,
        choices=category_choices,
        default='history',
    )
    description = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    youtube_url = models.CharField(max_length=50, default = " ")
    likes = models.IntegerField(default = 0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Trip, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class TripImage(models.Model):
    trip = models.ForeignKey(Trip, related_name='images')
    image = models.ImageField()

