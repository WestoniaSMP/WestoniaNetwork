#!/bin/bash

# Set default environment file
envFile=".env.dev"

# Check if a parameter is provided
if [ ! -z "$1" ]; then
    envFile="$1"
fi

# Check if the specified environment file exists
if [ ! -f "$envFile" ]; then
    echo "Environment file \"$envFile\" not found."
    exit 1
fi

# Start Docker Compose with the specified environment file
docker-compose --env-file "$envFile" up -d
