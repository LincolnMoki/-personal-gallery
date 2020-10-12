from django.db import models
from cloudinary.models import CloudinaryField
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')    
    description = models.CharField(max_length =100)
    categorytags = models.ManyToManyField(Category)
    locationtags = models.ManyToManyField(Location)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

    class Meta:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        verbose_name_plural='images'

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos                                                                   