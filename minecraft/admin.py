from django.contrib import admin
from .models import gamemode, difficulty, server, version

# Register your models here.

admin.site.register(difficulty)
admin.site.register(gamemode)
admin.site.register(version)
admin.site.register(server)