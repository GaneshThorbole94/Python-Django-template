from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(requests):
    #return HttpResponse('<h1> Welcome to my page </h1>')
    return render(requests,'home.html')

def contacts(requests):
    #return HttpResponse('<h1> Welcome to my page </h1>')
    return render(requests,'contacts.html')

def trainings(requests):
    #return HttpResponse('<h1> Welcome to my page </h1>')
    return render(requests,'trainings.html')

def shortcodes(requests):
    #return HttpResponse('<h1> Welcome to my page </h1>')
    return render(requests,'shortcodes.html')

def shows(requests):
    #return HttpResponse('<h1> Welcome to my page </h1>')
    return render(requests,'shows.html')

def classes(requests):
    #return HttpResponse('<h1> Welcome to my page </h1>')
    return render(requests,'classes.html')