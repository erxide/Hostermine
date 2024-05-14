from django.urls import path, include
from .views import delconf

urlpatterns = [
    path('getconf/', delconf, name='getconf'),
]