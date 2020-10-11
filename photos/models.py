from django.db import models
from cloudinary import CloudinaryImage
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryImage('image')
