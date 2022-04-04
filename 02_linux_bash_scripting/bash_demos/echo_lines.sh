#!/bin/bash
echo First arg is $1
for line in $(grep "HAMLET" ../hamlet.txt); do
	echo Found Line: $line
done
