from django.shortcuts import render, HttpResponseRedirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),  
    path('contact/',views.contact, name='contact'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('order_book/', views.order_book, name='order_book'),  
]
