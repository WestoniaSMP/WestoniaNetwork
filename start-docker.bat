@echo off
setlocal

REM Set default environment file
set "envFile=.env.dev"

REM Check if a parameter is provided
if not "%1"=="" (
    set "envFile=%1"
)

REM Check if the specified environment file exists
if not exist "%envFile%" (
    echo Environment file "%envFile%" not found.
    exit /b 1
)

REM Set the environment file for Docker Compose
set "COMPOSE_ENV_FILE=%envFile%"

REM Start Docker Compose
docker-compose --env-file "%COMPOSE_ENV_FILE%" up -d

endlocal