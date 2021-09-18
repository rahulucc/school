from django.db import models

# Create your models here.
class image(models.Model):
    pic=models.ImageField(upload_to="documents", blank=False)
