#!/bin/bash
# take a message as an argument and commit the changes to the repository

git add .
git commit -m "$1"
git push

# Read all lines from the file "app.env"
while read -r line; do
  # Split the line into key and value
  key=$(echo $line | cut -d'=' -f1)
  value=$(echo $line | cut -d'=' -f2)

  # Log the key and value
  echo "Setting key: $key, value: $value"

  # Run the "gh secret set" command with the key and value
  gh secret set $key -b $value

  # Check the exit code of the command
  if [ $? -ne 0 ]; then
    # If the exit code is non-zero, log an error
    echo "Error: gh secret set command failed"
  fi
done < app.env