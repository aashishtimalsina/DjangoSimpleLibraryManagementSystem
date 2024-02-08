from django.contrib import admin
from .models import ContactMessage

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(ContactMessage,ContactAdmin)
