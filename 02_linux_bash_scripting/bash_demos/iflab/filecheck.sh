#!/bin/bash
set -e

if [ $# = 0 ]; then
	echo "Script was run with no arguments. Try again."
	exit 1
fi

filename=$1

if [ ! -e $filename ]; then
	echo "File does not exist"
	exit 1
fi
