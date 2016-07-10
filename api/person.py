from django.db import models

class Person(models.Model):
    idPerson = models.IntegerField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
