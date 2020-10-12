from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome, name='home'),
    path('search/',views.search, name='search'),
    path('photos/(\d+)',views.photos,name ='photos')
   
]


