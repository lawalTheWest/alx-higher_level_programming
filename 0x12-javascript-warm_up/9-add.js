#!/usr/bin/node

// function that adds two integers
function add (a, b) {
  return a + b;
} /* End function */
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
