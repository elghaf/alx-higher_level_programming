#!/bin/bash

# Add all changes to the staging area
git add .

# Commit changes with a provided commit message or use a default message
commit_message="Default commit message"
if [ $# -eq 1 ]; then
    commit_message=$1
fi

git commit -m "$commit_message"

# Push changes to the remote repository
git push

