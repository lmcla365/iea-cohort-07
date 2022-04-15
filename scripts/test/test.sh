#!/bin/bash

if [ $# = 0 ]; then
    echo "Script was run with no arguments. Try again."
else
    for x in "$@"; do
         if [ -s $x ]; then
            mv $x $x'_inspectedByChris'
        else
           echo "The file $x is either empty or does not exits"
	   rm -f $x # > /dev/null 2>&1
        fi
     done
fi
