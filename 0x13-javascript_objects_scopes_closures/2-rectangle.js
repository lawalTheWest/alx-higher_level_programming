#!/usr/bin/node
/* Defines the Rectangle class */

class Rectangle {
  /* defines rectangle */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } /* end if */
  } /* ends constructor */
} /* End class */
module.exports = Rectangle;
