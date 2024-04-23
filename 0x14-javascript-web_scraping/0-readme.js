#!/usr/bin/node

/*
 * Importing the 'fs' module,
 * which provides functions for interacting with
 * the file system.
 */
const file_system = require('fs');
/*
 * Retrieving the third argument from
 * the command line, which is
 * expected to be the file path to be read.
 */
const file = process.argv[2];
/*
 * Reading the contents of the
 * specified file asynchronously.
 * 'utf-8' specifies the encoding of
 * the file to be read as UTF-8.
 * A callback function is provided to
 * handle the result of the file read operation.
 */

file_system.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
