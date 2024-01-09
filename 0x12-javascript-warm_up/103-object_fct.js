#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
}; /* end object */
console.log(myObject);

myObject.incr = function () {
  this.value++;
}; /* end functoin */

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
