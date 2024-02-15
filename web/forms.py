from django import forms
from contact.models import ContactMessage
from bookstore.models import bookOrder


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class BookOrderForm(forms.ModelForm):
    class Meta:
        model = bookOrder
        fields = ['customer_name', 'email', 'phone', 'coupon', 'book']
       