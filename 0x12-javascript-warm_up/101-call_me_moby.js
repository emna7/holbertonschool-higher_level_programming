#!/usr/bin/node
module.exports.callMeMoby = function(x, TheFunction) {
  let i;
  for (i = 0; i < x; i++) {
    TheFunction();
  }
};
