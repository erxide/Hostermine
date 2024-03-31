from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text="Votre nom d'utilisateur ne doit pas dépasser 30 caractères.", label="Nom d'Utilisateur")  # Vous pouvez définir la longueur maximale souhaitée

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
