#!/bin/bash -e
old_image_id=$(docker images -q jupyter-ir)
docker ps -a | grep ir_project && docker container rm ir_project

COMPOSE_DOCKER_CLI_BUILD=1 \
DOCKER_BUILDKIT=1 \
DOCKER_DEFAULT_PLATFORM=linux/amd64 
docker-compose build

docker image rm $old_image_id

./start.sh
