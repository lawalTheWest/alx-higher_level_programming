#!/usr/bin/node

const file_system = require('fs');
const file = process.argv[2];
const string = process.argv[3];

file_system.writeFile(file, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
