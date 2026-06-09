/**
 * shipfast-api · Node App
 * Simple utility functions used for CI/CD training demos.
 */

/**
 * Returns the sum of a and b.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function add(a, b) {
  return a + b;
}

/**
 * Returns a minus b.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function subtract(a, b) {
  return a - b;
}

/**
 * Returns a multiplied by b.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function multiply(a, b) {
  return a * b;
}

/**
 * Returns a divided by b.
 * Throws an error if b is zero.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

/**
 * Returns true if n is even, false otherwise.
 * @param {number} n
 * @returns {boolean}
 */
function isEven(n) {
  return n % 2 === 0;
}

module.exports = { add, subtract, multiply, divide, isEven };
