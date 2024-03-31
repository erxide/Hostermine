#!/bin/bash

# Auteur : Erwan SINCK
# Description : Ce script permet de supprimer le répertoire du serveur de jeu d'un utilisateur
# Date de création : 14/03/2024
# Date de dernière modification : 14/03/2024
# Version : 1.0

# Usage : ./sup_server.sh <username>

# Code du script commence ici...


# Vérification des arguments
if [ -z $1 ]; then
    echo "Il manque un argument" >&2
    exit 1
fi

# Affectation des arguments

user=$1

cd servers_mc   

# Suppression du répertoire du serveur de l'utilisateur
if [ -r  server_de_$user/ ]; then
    rm -r server_de_$user/
else 
    echo "$user n'a pas de serveur" >&2
    exit 1
fi