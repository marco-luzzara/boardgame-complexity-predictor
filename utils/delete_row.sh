#!/bin/bash
# usage ./delete_row.sh line_num filename

if (( $# != 2 ))
then
	exit 1
fi

sed "${1}d" "$2" > "${2}_fixed"
