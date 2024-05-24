#!/bin/bash

POKEMON_LIST="pokemon_list.txt"

BASE_URL="https://pokeapi.co/api/v2/pokemon-species"

OUTPUT_DIR="pokemon_data"

mkdir -p "$OUTPUT_DIR"

while IFS= read -r pokemon
do
    URL="$BASE_URL/$pokemon"

    OUTPUT_FILE="$pokemon.json"

    curl -s -o "$OUTPUT_FILE" "$URL"

    if [[ $? -eq 0 ]]; then
        echo "Downloaded data for $pokemon"
    else
        echo "Failed to download data for $pokemon"
    fi
sleep 2
done < "$POKEMON_LIST"
