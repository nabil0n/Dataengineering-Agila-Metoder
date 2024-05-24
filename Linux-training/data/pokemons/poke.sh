#!/bin/bash
while IFS= read -r line; do
    echo "pokemon: $line"
done < pokemon_list.txt
