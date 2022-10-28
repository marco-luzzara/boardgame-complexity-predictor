#!/bin/bash
# make sure to have a bgg.env file containing the following variables:
# BGGUSERNAME
# BGGPASSWORD

docker-compose up -d 

sleep 5

show_logs_command="docker logs --tail 5 ir_project 2>&1"
while [[ -z $(eval $show_logs_command | grep "To access the server") ]] ; do : ; done ;

eval $show_logs_command

