#!/bin/bash
# displays status code only; Usage: ./100-status_code.sh 0.0.0.0:5000/nop ;
curl -o /dev/null -w '%{http_code}' -sLI "$1"
