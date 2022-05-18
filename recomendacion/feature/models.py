from django.db import models

# Create your models here.

class caracteristicas(models.Model):
    docNumpy = models.FileField(upload_to='caracteristicas/')