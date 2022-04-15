#!/bin/bash

edate=`date --date="$1" +'%s'`
date=`date -d @$edate`

echo "The execution time is set to $date"
echo "The current working directory is `pwd`"
read -p "Enter Y to continue: " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
for image in $(du -a | awk '{print $2}'|xargs file --mime-type {} | grep image\/ | awk -F : '{print $1}');do
	file=`stat -c %Y $image`
	if [ $edate -gt $file ]; then 
		echo "The file $image would be moved"
	fi
done
else
	echo
	echo 'Thank you. Come again.'
fi
