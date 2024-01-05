#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message

curl -s -L -X PUT -d "user_id=98" "$1/catch_me" -H "Origin: HolbertonSchool"
