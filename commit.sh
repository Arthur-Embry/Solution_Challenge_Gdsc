#!/bin/bash
# take a message as an argument and commit the changes to the repository

git add .
git commit -m "$1"
git push


# find all key value pairs in app.env and commit with gh secret set foo -b bar

gh secret set "test" -b "test"