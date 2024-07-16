from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('createProfile/', ProfileCreateView.as_view(), name='create_profile'),
    path('createDevice/', DeviceCreateView.as_view(), name='create_device'),
]