from dataclasses import dataclass
from pyexpat import model
from django.db import models

# Create your models here.

class familiar(models.Model):

     nombre = models.CharField(max_length=30)

   