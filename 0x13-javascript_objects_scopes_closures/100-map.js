#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let i = 0;
const newList = list.map(function (x) {
  i++;
  return x * i;
})
console.log(newList);
