#!/bin/bash
# usage: ./find_biggest_doc.sh folder_if_exists/filename.csv

if (( $# != 1 ))
then
	exit 1
fi

biggest_doc=0
biggest_len=0

for i in $(seq 1 $(wc -l $1 | awk '{print $1}'))
do
	cur_len=$(cat $1 | head -${i} | tail +${i} | wc --chars )
	if (( $cur_len > $biggest_len ))
	then
		biggest_doc=$i
		biggest_len=$cur_len
	fi
done

echo "Biggest len: ${biggest_len}\nBiggest doc_ ${biggest_doc}"
