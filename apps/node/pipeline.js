/**
 * shipfast-api · Node App
 * Pipeline module — chains utility functions together.
 * Used for integration testing demos.
 */

const { add, subtract, multiply, divide, isEven } = require("./utils");

/**
 * Apply a percentage discount to a price.
 * @param {number} price
 * @param {number} discountPercent
 * @returns {number}
 */
function calculateDiscount(price, discountPercent) {
  const discount = divide(multiply(price, discountPercent), 100);
  return subtract(price, discount);
}

/**
 * Sum a list of item prices.
 * @param {number[]} items
 * @returns {number}
 */
function calculateTotal(items) {
  return items.reduce((total, price) => add(total, price), 0);
}

/**
 * Calculate the average of a list of numbers.
 * @param {number[]} items
 * @returns {number}
 */
function calculateAverage(items) {
  if (items.length === 0) {
    throw new Error("Cannot divide by zero");
  }
  return divide(calculateTotal(items), items.length);
}

/**
 * Return true if quantity qualifies as a bulk order.
 * @param {number} quantity
 * @param {number} threshold
 * @returns {boolean}
 */
function isBulkOrder(quantity, threshold = 10) {
  return quantity >= threshold;
}

module.exports = { calculateDiscount, calculateTotal, calculateAverage, isBulkOrder };