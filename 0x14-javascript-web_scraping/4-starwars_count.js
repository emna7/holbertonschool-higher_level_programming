#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
  const list = JSON.parse(body).results;
  let nb = 0;
  for (const film of list) {
    if (filmcharacters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        nb++;
      }
    }
    console.log(nb);
  }
});
