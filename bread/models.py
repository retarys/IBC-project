from django.db import models

class person(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()



