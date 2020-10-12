from django.shortcuts import render
fr.om django.http import HttpResponse
import datetime as dt
from .models import Image
def welcome(request):
    title = 'welcome'
    Image = Image.objects.all()
    return render(request,'photos/home.html', {'title': title, 'images':images})

def dynamic_urls(request, query):
    q_object = query
    return HttpResponse(q_object)