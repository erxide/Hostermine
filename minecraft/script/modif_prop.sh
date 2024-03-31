#!/bin/bash

#  Auteur : Erwan SINCK
#  Description : Ce script permet de modifier les propriétés d'un serveur Minecraft
#  Date de création : 14/03/2024
#  Date de dernière modification : 14/03/2024
#  Version : 1.0

# Usage : ./modif_prop.sh <username> <server_name> <max_players> <gamemode> <difficulty> <whitelist> <online_mode> <pvp> <command_block> <allow_flight> <spawn_animals> <spawn_monsters> <spawn_npcs> <allow_nether> <force_gamemode> <spawn_protection>

# Code du script commence ici...

# Vérification des arguments
if [ -z "$16" ]; then
    echo "Il manque un argument" >&2
    exit 1
fi

# Affection des arguments
user="$1"
server_name=$(echo $2 | sed 's/_/ /g')                      # Remplacer les _ par des espaces
max_players="$3"
gamemode="$4"
difficulty="$5"
whitelist=$(echo $6 | tr '[:upper:]' '[:lower:]')           # Mettre en minuscule
online_mode=$(echo $7 | tr '[:upper:]' '[:lower:]')         # Mettre en minuscule
pvp=$(echo ${8} | tr '[:upper:]' '[:lower:]')               # Mettre en minuscule
command_block=$(echo $ | tr '[:upper:]' '[:lower:]')        # Mettre en minuscule
allow_flight=$(echo ${10} | tr '[:upper:]' '[:lower:]')     # Mettre en minuscule
spawn_animals=$(echo ${11} | tr '[:upper:]' '[:lower:]')    # Mettre en minuscule
spawn_monsters=$(echo ${12} | tr '[:upper:]' '[:lower:]')   # Mettre en minuscule
spawn_npcs=$(echo ${13} | tr '[:upper:]' '[:lower:]')       # Mettre en minuscule
allow_nether=$(echo ${14} | tr '[:upper:]' '[:lower:]')     # Mettre en minuscule
force_gamemode=$(echo ${15} | tr '[:upper:]' '[:lower:]')   # Mettre en minuscule
spawn_protection="${16}" 

# Aller dans le répertoire du serveur de l'utilisateur
cd "servers_mc/server_de_$user"

# Récupération des deux premières lignes du fichier server.properties
headers=$(head -n 2 server.properties)

# Modification du fichier server.properties
printf "%s\n%s" "$headers" "enable-jmx-monitoring=false
rcon.port=25575
level-seed=
gamemode=$gamemode
enable-command-block=$command_block
enable-query=false
generator-settings={}
enforce-secure-profile=false
level-name=world
motd=$server_name
query.port=25565
pvp=$pvp
generate-structures=true
difficulty=$difficulty
network-compression-threshold=256
max-tick-time=60000
use-native-transport=true
max-players=$max_players
online-mode=$online_mode
enable-status=true
allow-flight=$allow_flight
initial-disabled-packs=
broadcast-rcon-to-ops=true
view-distance=10
server-ip=
resource-pack-prompt=
allow-nether=$allow_nether
server-port=25565
enable-rcon=false
sync-chunk-writes=true
resource-pack-id=
op-permission-level=4
prevent-proxy-connections=false
resource-pack=
entity-broadcast-range-percentage=100
simulation-distance=10
rcon.password=
player-idle-timeout=0
force-gamemode=$force_gamemode
rate-limit=0
hardcore=false
white-list=$whitelist
broadcast-console-to-ops=true
spawn-npcs=$spawn_npcs
spawn-animals=$spawn_animals
logs-ips=false
function-permission-level=2
initial-enabled-packs=vannila
level-type=minecraft\:normal
text-filtering-config=
spawn-monsters=$spawn_monsters
enforce-whitelist=false
spawn-protection=$spawn_protection
resource-pack-sha1=
max-world-size=29999984" > server.properties