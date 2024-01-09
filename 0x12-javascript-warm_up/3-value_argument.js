#!/usr/bin/node

// Script that prints the first argument
const arg = process.argv[2];

if (arg === undefined) {
  console.log('No argument');
} /* End if */ else {
  console.log(arg);
} /* end else */
