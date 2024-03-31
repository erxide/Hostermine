#!/bin/bash

# Auteur: Erwan SINCK
# Description: Ce script permet de créer un répertoire pour un utilisateur avec la version de Minecraft de son choix
# Date de création: 13/03/2024
# Date de dernière modification: 13/03/2024
# Version : 1.0

# Usage : ./create_user_dir.sh <username> <version>

# Code du script commence ici...

# Vérification des arguments
if [ -z "$2" ]; then
    echo "Il manque un argument">&2
    exit 1
fi

# Affection des arguments
username=$1
version=$2

# Création du répertoire
mkdir -p servers_mc

# Vérification de l'existence du répertoire
if [ -d "servers_mc/server_de_$username" ]; then
    echo "L'utilisateur $username a déjà un serveur de jeu">&2
    exit 1
fi

# Création du répertoire
mkdir -p "servers_mc/server_de_$username"

cp -r "minecraft/version/$version/"* "servers_mc/server_de_$username"

echo "ok"
