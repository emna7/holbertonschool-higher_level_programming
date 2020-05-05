#!/usr/bin/node
function factorial (x) {
  if (x === 0 || !Number(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
