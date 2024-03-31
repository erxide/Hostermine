from django.contrib import admin
from django.urls import path
from .views import test

urlpatterns = [
    path('', test, name='test'),
]