#!/bin/bash

# Auteur : Erwan SINCK
# Description : Ce script permet de lancer le serveur de jeu d'un utilisateur
# Date de création : 19/03/2024
# Date de dernière modification : 19/03/2024
# Version : 1.0

# Usage : ./run_docker.sh <username>

# Code du script commence ici...

# Vérification des arguments
if [ -z $1 ]; then
    echo "Il manque un argument" >&2
    exit 1
fi

# Affectation des arguments
username=$1

cd servers_mc
cd server_de_$username

# Lancement du serveur
docker-compose up -d
