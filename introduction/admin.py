from django.contrib import admin
from .models import introduction

class IntroductioAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(introduction,IntroductioAdmin)
