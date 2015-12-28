# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'BusNo'
        verbose_name_plural = 'BusNo'
        ordering = ['name']

    def __str__(self):
        return self.name


class PublicRouteManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicRouteManager, self).get_queryset()
        return qs.filter(is_public=True)


@python_2_unicode_compatible
class Route(models.Model):
    url = models.URLField('Click me to connect with google maps?',max_length=255)
    title = models.CharField('Bus Route', max_length=255)
    latitude = models.CharField('Latitude',max_length=512)
    longitude = models.CharField('Longitude',max_length=512)
    
    is_public = models.BooleanField('Like my service?', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='Routes')
    BusNo = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    public = PublicRouteManager()

    class Meta:
        verbose_name = 'Bus Information'
        verbose_name_plural = 'Bus Information'
        ordering = ['-date_created']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Route, self).save(*args, **kwargs)
