#!/usr/bin/node

/* computes the factorial of a given number (argv) */
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
} /* ens function */

console.log(factorial(Number(process.argv[2])));
