#!/usr/bin/node
const fs = require('fs');
let path = process.argv[2];
let data = process.argv[3];
fs.writeFile(path, data, function (err) {
  if (err) {
    console.log(err);
  }
});
