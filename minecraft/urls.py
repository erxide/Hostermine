from django.urls import path, include
from .views import create_server, test_request, sup_server, modify_server

urlpatterns = [
    path('createserver/', create_server, name='create_server'),
    path('test/', test_request, name='test'),
    path('supserver/', sup_server, name='sup_server'),
    path('modifyserver/', modify_server, name='modify_server'),
]