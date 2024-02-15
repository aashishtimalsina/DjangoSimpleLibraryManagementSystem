from django.shortcuts import render, redirect,HttpResponseRedirect
from web.forms import ContactMessageForm
from web.forms import BookOrderForm
from django.contrib import messages
from bookstore.models import book
from introduction.models import introduction

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


def order_book(request):
    if request.method == 'POST':
        form = BookOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = BookOrderForm()
    return render(request, 'order_book.html', {'form': form})