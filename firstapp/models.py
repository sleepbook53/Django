from django.db import models

# Create your models here.
#class name = table name
#vlaues = index name
#made model  => created DB
class Curriculum(models.Model) :
    name = models.CharField(max_length=255)