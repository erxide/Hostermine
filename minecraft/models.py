from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from random import randint


class gamemode(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    realname = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Gamemode"
        verbose_name_plural = "Gamemodes"


class difficulty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    realname = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Difficulty"
        verbose_name_plural = "Difficulties"

class version(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"

def default_whitelist():
    return {"whitelist": []}

def get_last_version():
    return version.objects.latest('release_date').id

def get_default_difficulty():
    return difficulty.objects.get(name="Normale").id

def get_default_gamemode():
    return gamemode.objects.get(name="survie").id

def get_port():
    while True:
        port = randint(25565, 26565)
        try:
            if not server.objects.filter(port=port).exists():
                return port
        except:
            return port

class server(models.Model):
    name = models.CharField(max_length=100, default="Minecraft Server")
    port = models.IntegerField(default=get_port, validators=[MaxValueValidator(26565), MinValueValidator(25565)], blank=True)
    version = models.ForeignKey(version, on_delete=models.SET_NULL, null=True, default=get_last_version)
    max_players = models.IntegerField(default=20, validators=[MaxValueValidator(20), MinValueValidator(1)])
    gamemode_id = models.ForeignKey(gamemode, on_delete=models.SET_NULL, null=True, default=get_default_gamemode)
    difficulty_id = models.ForeignKey(difficulty, on_delete=models.SET_NULL, null=True, default=get_default_difficulty)
    whitelist_enabled = models.BooleanField(default=False)
    whitelist = models.JSONField(default=default_whitelist)
    online_mode = models.BooleanField(default=True)
    pvp_enabled = models.BooleanField(default=True)
    command_block_enabled = models.BooleanField(default=False)
    allow_flight = models.BooleanField(default=False)
    spawn_animals = models.BooleanField(default=True)
    spawn_monsters = models.BooleanField(default=True)
    spawn_npcs = models.BooleanField(default=True)
    allow_nether = models.BooleanField(default=True)
    force_gamemode = models.BooleanField(default=False)
    spawn_protection = models.IntegerField(default=16, validators=[MaxValueValidator(20), MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"


