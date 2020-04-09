#!/bin/bash
# a Bash script that takes in a URL and displays
curl -sI "$1" | sed -n 's/Allow: //p'
