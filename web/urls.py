from django.shortcuts import render
from django.urls import path
from bookstore.models import book
from introduction.models import introduction
from contact.views import contact_view


def home(request):
    books = book.objects.all()  
    return render(request, 'index.html', {'books': books})


def about(request):
    introductions = introduction.objects.all()  
    return render(request, 'about.html', {'introductions': introductions})

def contact(request):
    return render(request, 'contact.html')


urlpatterns = [
    path('', home, name='home'),  
    path('about/', about, name='about'),  
    path('contact/',contact_view, name='contact'),
]
