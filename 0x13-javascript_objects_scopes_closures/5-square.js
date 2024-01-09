#!/usr/bin/node

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  } /* End the contructor class */
}; /* end the rectangle class */
