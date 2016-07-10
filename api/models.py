from __future__ import unicode_literals

from django.db import models
# Models

class People(models.Model):
    id_person = models.BigIntegerField
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
