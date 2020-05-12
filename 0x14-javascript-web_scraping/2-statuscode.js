#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
request(url, function (err, url) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + url.statusCode);
  }
});
