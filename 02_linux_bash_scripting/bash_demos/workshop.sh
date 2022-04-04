#!/bin/bash

filelist="$(ls -R1 ./)"

for line in "$filelist"; do
	if echo "$line" | grep ":$"; then
		dir="$(echo $line | grep -oP '[^:]+')"
		echo $dir
	else
		if file "$dir/$line" | grep "\bimage\b"; then
			echo "$line is an image"
		fi
	fi
done
