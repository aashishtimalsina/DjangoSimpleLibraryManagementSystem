from django.shortcuts import render
from django.urls import path


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


urlpatterns = [
    path('', home, name='home'),  
    path('about/', about, name='about'),  
    path('contact/', contact, name='contact'),    
]
