#!/bin/bash
# usage ./select_valid_rulebooks.sh filename

if (( $# != 1 ))
then
	exit 1
fi

docs_to_delete=()

for i in $(seq 1 $(wc -l "$1" | awk '{print $1}'))
do
	echo "======================================== $i"
	echo "$(cat "$1" | head -${i} | tail -1)"
	
	echo "You want to keep it (line $i)? (y or [ENTER]/n)"
	read answer
	
	if [[ $answer == 'n' ]]
	then
		docs_to_delete+=( $i )
	fi
done

stringed_array="${docs_to_delete[@]}"
sed_string="${stringed_array// /d;}d"
echo "$sed_string"

if [[ $sed_string != 'd' ]]
then
	sed "${sed_string}" "$1" > "${1}_valid"
fi

