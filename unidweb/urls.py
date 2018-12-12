from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unid/', include('unid.urls')),
    url(r'^accounts/', include('allauth.urls')),
]
