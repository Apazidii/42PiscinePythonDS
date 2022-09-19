#!/bin/sh

if [ $# -ne 0 ]
	then
		TEXT=$1
	else
		TEXT='data scientist'
fi

URL='https://api.hh.ru/vacancies'

echo 123

curl -H 'User-Agent: loh' -G $URL		\
--data-urlencode 'per_page=20'			\
--data-urlencode 'page=0'				\
--data-urlencode 'search_field=name'	\
--data-urlencode "text=$TEXT"			| jq > hh.json
