#!/usr/bin/node

// script that prints x times “C is fun”
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} /* End if */ else {
  for (let index = 0; index < x; index++) {
    console.log('C is fun');
  } /* end for */
} /* end else */
