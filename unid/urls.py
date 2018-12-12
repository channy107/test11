
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('contentmain/', contentmain),
    path('mywallet/', mywallet),
]
