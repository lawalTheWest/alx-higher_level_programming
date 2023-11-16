#!/usr/bin/node

// searches the seond biggest integer in the list of arguments
/* validate parameters */
if (process.argv.length <= 3) {
  console.log(0);
} /* end if */ else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} /* end else */
