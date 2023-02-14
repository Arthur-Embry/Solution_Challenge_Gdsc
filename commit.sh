#!/bin/bash
# Function that takes a message as an argument and commits the changes to the repository

git add .
git commit -m "$1"
git push
