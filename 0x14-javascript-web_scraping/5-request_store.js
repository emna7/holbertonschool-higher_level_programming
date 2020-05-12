#!/usr/bin/node
const filesystem = require('fs');
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    filesystem.writeFile(process.argv[3], body, 'utf8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
