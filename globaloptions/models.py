from django.db import models
from django.contrib.sites.models import Site
# Create your models here.

class GlobalOptions(models.Model):
    site = models.ForeignKey(Site)
    sitename = models.CharField(max_length=200)
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Global Site Options'
