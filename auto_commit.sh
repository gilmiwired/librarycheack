#!usr/bin/bash

while true
do
	git pull
	git add .
	git commit -m 'auto commit'
	sleep 100
done
