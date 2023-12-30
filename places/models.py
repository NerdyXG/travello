from django.db import models

# Create your models here.

class Destination(models.Model):
    image = models.ImageField(upload_to="destination_imgs")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    special_offer = models.BooleanField(default=False)