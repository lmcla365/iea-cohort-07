#!/bin/bash

#check for single arg
if [ $# != 1 ]; then
    echo "Script requires a repository name as an arguement."
    exit 1
else
    repo=$1
fi

#check for/create GIT dir in user's home
if [ ! -d ~/GIT/$repo ]; then
    `mkdir -p ~/GIT/$repo`
#    cd  ~/GIT/$repo
#    echo `pwd`
else
    echo "A directory with the name $repo exists in `pwd`/GIT"
    exit 2
fi

`git init ~/GIT/$repo --quiet`
if [ $? != 0 ]; then
    echo "There was a problem inilitizing the repository"
    exit 3
fi

`curl -s -o ~/GIT/$repo/.gitignore "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"`
if [ $? != 0 ]; then
    echo "There was an issue downloading .gitignore"
    exit 4
fi

echo ".gitignore file"
echo "-----------------------------------------"
more ~/GIT/$repo/.gitignore
echo -e "\nYou successfully initiated the git repo ~/GIT/$repo\n"
