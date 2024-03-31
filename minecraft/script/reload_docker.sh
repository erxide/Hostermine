
# Vérification des arguments
if [ -z $1 ]; then
    echo "Il manque un argument" >&2
    exit 1
fi

# Affectation des arguments
username=$1

cd servers_mc
cd server_de_$username


docker-compose down
docker-compose up -d