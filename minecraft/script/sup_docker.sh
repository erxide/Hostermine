#!/bin/bash

# Auteur : Erwan SINCK
# Description : Ce script permet de supprimer le docker du serveur de jeu d'un utilisateur
# Date de création : 19/03/2024
# Date de dernière modification : 19/03/2024
# Version : 1.0

# Usage : ./sup_docker.sh <username>

# Code du script commence ici...

# Vérifie si un nom d'utilisateur est fourni en argument
if [ $# -eq 0 ]; then
    echo "Veuillez fournir un nom d'utilisateur en argument."
    exit 1
fi

# Récupère le nom d'utilisateur passé en argument
username=$1

# Vérifie si le docker de l'utilisateur existe
docker=$(docker ps -a --format '{{.Names}}' | grep "serveur_de_$username")

echo $docker

if [ -n "$docker" ]; then  # Si le docker existe
    # Supprime le docker
    docker kill "$docker"
    docker rm "$docker"
    echo "Le serveur de $username a été supprimé."
else
    echo "Le serveur de $username n'existe pas."
    exit 1
fi
