from django.shortcuts import render, HttpResponseRedirect
from django.urls import path
from bookstore.models import book
from introduction.models import introduction
from web.forms import ContactMessageForm 
from django.contrib import messages


def home(request):
    books = book.objects.all()  
    return render(request, 'index.html', {'books': books})


def about(request):
    introductions = introduction.objects.all()  
    return render(request, 'about.html', {'introductions': introductions})

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return HttpResponseRedirect('/success/')  # Redirect to a success page
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

urlpatterns = [
    path('', home, name='home'),  
    path('about/', about, name='about'),  
    path('contact/',contact, name='contact'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
]
