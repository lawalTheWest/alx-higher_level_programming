#!/usr/bin/node
const request = require('request');
const file_system = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    file_system.writeFileSync(process.argv[3], body);
  }
});
