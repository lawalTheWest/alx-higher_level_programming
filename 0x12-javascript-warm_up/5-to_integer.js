#!/usr/bin/node

/*
 * script that prints:
 * My number: <first argument converted in integer>
 * if the first argument can be converted to an intege
 */

const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Not a number');
} /* end if */ else {
  console.log('My number:' + num);
} /* End else */
