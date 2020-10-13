from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome, name='home'),
    path('search/',views.search_image, name='search_image'),
    path('photos/(\d+)',views.photos,name ='photos')
   
]


