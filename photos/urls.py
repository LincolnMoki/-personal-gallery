from django.urls import path
from .views import welcome
urlpatterns = [
    path('',welcome, name='home'),
    #path('search/',views.search name='search')
   
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)