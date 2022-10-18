#!/bin/bash
old_image_id=$(docker images -q jupyter-ir)
docker container rm  ir_project
docker-compose build

docker image rm $old_image_id

./start.sh
