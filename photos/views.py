from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image
def welcome(request):
    title = 'welcome'
    images = Image.objects.all()
    return render(request,'photos/home.html', {'title': title, 'images':images})


def search(request):
    if "term" in request.GET and request.GET["term"]:
        term = request.GET.get("term")
        photos = Image.search_image(term)
        if photos != "No images found":
            message = "Photos of '" + term + "'"
            return render(request, "search.html", {"images":photos,"message":message,"title":term.capitalize()})
        else:
            message = "No images found"
            return render(request, "search.html", {"images":[],"message":message,"title":term.capitalize()})
    
  
def photos(request,photos_id):
    try:
        photos = Photos.objects.get(id = photos_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery/photos.html", {"photos":photos})    