#!/bin/bash
# Takes in URL, displays body of a 200 response; Usage: ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
curl -sL "$1"
