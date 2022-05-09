from django.conf import settings
from django.db import models
class Datesheet(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    day = models.DateField(null=True,blank=True,)
    time = models.TimeField(null=True,blank=True,)

# Create your models here.
