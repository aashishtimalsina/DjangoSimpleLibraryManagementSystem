from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),    
]

admin.site.index_title = "Hamrobooks"
admin.site.site_header = "Hamrobooks Admin"
admin.site.site_title = "Admin Portal"