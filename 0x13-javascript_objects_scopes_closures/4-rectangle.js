#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; } /* ends if */
  } /* ends The constructor class */

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    } /* End the for statement */
  } /* Ends the print function */

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  } /* End the rotate function */

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  } /* End the double function */
}; /* end the rectangle class */
