from django.db import models
from django.contrib.sites.models import Site

# Create your models here.


class AboutOptions(models.Model):
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=200,blank=True)
    intro = models.TextField(max_length=1000,blank=True)
    maintext = models.TextField(max_length=1000,blank=True)
    outro = models.TextField(max_length=1000,blank=True)
    backgroundImage = models.ImageField(upload_to='static')

    class Meta:
        verbose_name_plural = 'About Page Options'
