from django.shortcuts import render, redirect,HttpResponseRedirect
from web.forms import ContactMessageForm
from web.forms import BookOrderForm
from django.contrib import messages
from bookstore.models import book
from introduction.models import introduction
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

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

# def order_book(request):
#     if request.method == 'POST':
#         form = BookOrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Order placed successfully'})
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)

def order_book(request):
    if request.method == 'POST':
        form = BookOrderForm(request.POST)
        if form.is_valid():
            instance = form.save()
            send_instant_reply_email(instance) 
            return JsonResponse({'message': 'Order placed successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def send_instant_reply_email(order_instance):
    subject = 'Hamro Books'
    message = 'Thank you for your book order! We will be in touch with you shortly'
    from_email = settings.EMAIL_HOST_USER
    to_email = [order_instance.email]
    
    try:
        send_mail(subject, message, from_email, to_email)  
        print("Instant reply email sent successfully.")
    except Exception as e:
        print("An error occurred while sending the instant reply email:", e)