#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of the response (only for 200 status code)

curl -sL -w "%{http_code}" "$1" -o /dev/null
