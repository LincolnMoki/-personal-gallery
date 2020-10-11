from django.shortcuts import render

def welcome(request):
    title = 'welcome'
    return render(request,'photos/home.html', {'title': title})
