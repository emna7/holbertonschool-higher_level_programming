#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += 'X';
      }
      console.log(result);
    }
  }

  rotate () {
    const a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.height = (this.height * 2);
    this.width = (this.width * 2);
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
