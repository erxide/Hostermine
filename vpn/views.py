from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import CustomUser
import requests
import subprocess
from pathlib import Path
import os


# Create your views here.
def createconf(user: CustomUser):
    if not os.path.exists(f"vpn/confvpn/{user.username}.ovpn"):
        response = requests.get(f"http://localhost:8080/{user.username}")
        info = response.json()
        subprocess.run([f"{Path(__file__).resolve().parent}/script/createconf.sh {user.username} '{info['crt']}' '{info['key']}'"], shell=True, capture_output=True, text=True)
   
def delconf(request):
    user = CustomUser.objects.get(id=request.user.id)
    with open(f"vpn/confvpn/{user.username}.ovpn", 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{user.username}.ovpn"'
        return response