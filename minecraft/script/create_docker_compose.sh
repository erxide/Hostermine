#!/bin/bash

# Auteur : Erwan SINCK
# Description : Ce script permet de créer un fichier docker-compose.yml pour un serveur Minecraft
# Date de création : 19/03/2024
# Date de dernière modification : 19/03/2024
# Version : 1.0

# Usage : ./create_docker_compose.sh <username> <port> <version>

# Code du script commence ici...

# Vérification des arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: create_docker_compose.sh <username> <port> <version>"
    exit 1
fi
 
# Affectation des arguments
username=$1
port=$2 
version=$3


cd servers_mc
cd server_de_$username

# Création du fichier docker-compose.yml
touch docker-compose.yml

# Remplissage du fichier docker-compose.yml
echo "version: '3.7'

services:
  minecraft_server:
    image: openjdk:latest
    container_name: serveur_de_$username
    ports:
      - $port:25565
    volumes:
      - .:/minecraft
    restart: always
    user: "1000:1000"
    command: sh -c 'cd /minecraft && java -Xmx1024M -Xms1024M -jar minecraft_server.$version.jar nogui'" > docker-compose.yml