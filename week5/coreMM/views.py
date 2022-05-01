from django.shortcuts import render
from django.http import HttpResponse

# return template
def home(request):
    return render(request, 'home.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def contactme(request):
    return render(request, 'contactme.html')

def schedulewme(request):
    return render(request, 'schedulewme.html')






