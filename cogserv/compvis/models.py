from distutils.command.upload import upload
from django.db import models

# Create your models here.
class OCRInput(models.Model):
    input_img = models.ImageField()