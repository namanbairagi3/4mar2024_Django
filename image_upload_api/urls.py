
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('imageapi.urls')),
    path('api/', include('customerApp.urls')),
    path('', include('myapp.urls')),
]

# http://primarydomain.com/api/createTask
# http://primarydomain.com/api/getBalalance

