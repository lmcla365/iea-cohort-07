#!/bin/bash
echo First arg is $1
for arg in "$*"; do
	echo $arg
done
