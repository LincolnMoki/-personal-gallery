from django.db import models
from cloudinary.models import CloudinaryField
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')    
    description = models.CharField(max_length =100)
    categorytags = models.ManyToManyField(Category)
    locationtags = models.ManyToManyField(Location)
    date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
       
        self.save()

    def delete_image(self):
       
        Image.objects.get(id = self.id).delete()


    def update_image(self,val):
       
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):
       
        return cls.objects.get(id = image_id)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def search_image(cls,category):
       
        try:   
            searched_category = Category.objects.filter(name__icontains  = category)[0]
            return cls.objects.filter(category_id = searched_category.id)
        except Exception:
            return "No images found"    

    def __str__(self):
        return self.title

    class Meta:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        verbose_name_plural='images'

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos     

class Location(models.Model):
   
    name = models.CharField(max_length = 30)

    def save_location(self):

        self.save()

    def delete(self):
       
        self.delete()

    def update(self,field,val):
        
        Location.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name


class Category(models.Model):
    
    name = models.CharField(max_length = 30)
    def save_category(self):
      
        self.save()

    def delete(self):
       
        Category.objects.get(id = self.id).delete()

    def update(self,field,val):
       
        Category.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name