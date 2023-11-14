#!/usr/bin/node

// prints based on arguments given
const { argv } = require('node:process');

// getting the lenght of arguments
const argvLength = argv.length - 2;

// validate parameters
if (argvLength <= 0) {
  console.log('No argument');
} /* end if */ else if (argvLength === 1) {
  console.log('Argument found');
} /* end else if */ else {
  console.log('Arguments found');
} /* end else */
