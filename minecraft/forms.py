from django import forms
from .models import server
from django.core.validators import RegexValidator

class serverForm(forms.ModelForm):

    name = forms.CharField(max_length=100, validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9 ]+$',
                message='Ce champ ne doit contenir que des lettres, des chiffres et des espaces.',
                code='invalid_characters'
            )
        ])

    class Meta:
        model = server
        fields = [
            'name',
            'version', 
            'max_players', 
            'gamemode_id', 
            'difficulty_id', 
            'whitelist_enabled', 
            'online_mode', 
            'pvp_enabled', 
            'command_block_enabled',
            'allow_flight', 
            'spawn_animals', 
            'spawn_monsters', 
            'spawn_npcs', 
            'allow_nether', 
            'force_gamemode', 
            'spawn_protection'
        ]
        labels = {
            'name':'Nom du serveur',
            'version':'Version',
            'max_players':'Nombre de joueur max',
            'gamemode_id':'Mode de jeu',
            'difficulty_id':'Difficulté',
            'whitelist_enabled':'Activer la Whitelist',
            'online_mode':'Mode en ligne',
            'pvp_enabled':'Activer pvp',
            'command_block_enabled':'Activer command block',
            'allow_flight':'Accepter le vol',
            'spawn_animals':'Faire apparaitre les animaux',
            'spawn_monsters':'Faire apparaitre les monstres',
            'spawn_npcs':'Faire apparaitre les villageois',
            'allow_nether':'Activer le nether',
            'force_gamemode':'Forcer le gamemode',
            'spawn_protection':'Zone de proctection de spawn'
        }