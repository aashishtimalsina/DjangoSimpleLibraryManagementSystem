from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('web.urls')),
    
]

admin.site.index_title = "Hamrobooks"
admin.site.site_header = "Hamrobooks Admin"
admin.site.site_title = "Admin Portal"
