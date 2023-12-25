#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <wordlist_file_path> <hashed_password>"
    exit 1
fi

# The 1st argument given from commmand line is the file path
# containing the word list to compare with the hashed password
wordlist_file_path="$1"
# The 2nd argument is the hashed password
hashed_pwd="$2"

# Check if the wordlist file exists
if [ ! -f "$wordlist_file_path" ]; then
    echo "Error: Wordlist file '$wordlist_file_path' not found."
    exit 1
fi

# Set IFS to an empty value to preserve spaces
IFS=
# Read each line from the word list file and compare it
# to the hashed password
while read -r word; do
	hashed_word=$(echo -n $word | md5sum | awk '{print $1}');

	if [[ "$hashed_word" == "$hashed_pwd" ]]; then
		echo -e "\033[32mHASHES MATCH FOR: '$word'\033[0m"
		echo "Found match, exiting..."
		break
	else
		echo "no match found for: '$word'";
	fi
done < "$wordlist_file_path"