#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(response.statusCode);
  }
});
