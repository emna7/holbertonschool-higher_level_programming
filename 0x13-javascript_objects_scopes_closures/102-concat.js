#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const fileA = process.argv[2];
const textA = fs.readFileSync(fileA, 'utf8');
const fileB = process.argv[3];
const textB = fs.readFileSync(fileB, 'utf8');
const fileC = process.argv[4];
fs.writeFileSync(fileC, textA);
fs.appendFileSync(fileC, textB);
