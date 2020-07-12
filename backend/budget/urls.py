from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls)
]
