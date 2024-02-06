from django.contrib import admin
from .models import book, bookCategory,bookOrder



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_date')
    search_fields = ('title', 'author')

class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name',)
    
admin.site.register(book,BookAdmin)
admin.site.register(bookCategory,BookCategoryAdmin)
admin.site.register(bookOrder,BookOrderAdmin)
