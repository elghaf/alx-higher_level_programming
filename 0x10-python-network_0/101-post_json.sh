#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument and displays the body of the response

filename="$2"

if [ -f "$filename" ]; then
    curl -sX POST -H "Content-Type: application/json" -d @"$filename" "$1"
else
    echo "File not found: $filename"
fi
