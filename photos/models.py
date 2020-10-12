from django.db import models
from cloudinary.models import Cloudinaryfield
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = Cloudinaryfield('image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='images'
