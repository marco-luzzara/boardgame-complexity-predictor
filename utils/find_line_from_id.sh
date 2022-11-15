#!/bin/bash
# usage: ./find_line_from_id.sh id filename.csv

if (( $# != 2 ))
then
	exit 2
fi

cat "$2" | grep --color=always -Eon ".{,40},${1},.{,40}"
