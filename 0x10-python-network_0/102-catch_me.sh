#!/bin/bash
# Bash script that sends a PUT request to the URL 0.0.0.0:5000/catch_me,
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
