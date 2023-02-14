#!/bin/bash
# take a message as an argument and commit the changes to the repository

git add .
git commit -m "$1"
git push


# find all key value pairs in app.env and commit with gh secret set foo -b bar
cat app.env | while read line; do
    key=$(echo $line | cut -d '=' -f 1)
    value=$(echo $line | cut -d '=' -f 2)
    gh secret set $key -b $value
done

# Read all lines from the file "app.env"
while read -r line; do
  # Split the line into key and value
  key=$(echo $line | cut -d'=' -f1)
  value=$(echo $line | cut -d'=' -f2)

  # Run the "gh secret set" command with the key and value
  gh secret set $key -b $value
done < app.env