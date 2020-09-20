from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length = 200)
    url = models.URLField(max_length=200)
    image= models.ImageField(upload_to='sponsors/', blank=True, null=True)

# Create your models here.
