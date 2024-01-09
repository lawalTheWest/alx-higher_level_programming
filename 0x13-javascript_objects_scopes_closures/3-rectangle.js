#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  } /*End the constructor */

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    } /* end the for statement */
  } /* End the print function */
}; /* End the rectangle class */
