from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('web.urls')),
    
]

admin.site.index_title = "Hamrobooks"
admin.site.site_header = "Hamrobooks Admin"
admin.site.site_title = "Admin Portal"

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
