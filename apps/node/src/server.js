#!/usr/bin/env node

const http = require("http");
const { add, subtract, multiply, divide } = require("./utils");
const {
  calculateDiscount,
  calculateTotal,
  calculateAverage,
  isBulkOrder
} = require("./pipeline");

const port = process.env.PORT || 3000;

function sendJson(response, statusCode, payload) {
  response.writeHead(statusCode, {
    "Content-Type": "application/json"
  });
  response.end(JSON.stringify(payload));
}

const server = http.createServer((request, response) => {
  if (request.url === "/") {
    sendJson(response, 200, {
      service: "shipfast-api-node",
      status: "running",
      message: "Node artifact deployed successfully"
    });
    return;
  }

  if (request.url === "/health") {
    sendJson(response, 200, {
      service: "shipfast-api-node",
      status: "healthy"
    });
    return;
  }

  if (request.url === "/calculate") {
    sendJson(response, 200, {
      add: add(10, 5),
      subtract: subtract(10, 5),
      multiply: multiply(10, 5),
      divide: divide(10, 5),
      discount: calculateDiscount(100, 10),
      total: calculateTotal([10, 20, 30]),
      average: calculateAverage([10, 20, 30]),
      bulkOrder: isBulkOrder(15)
    });
    return;
  }

  sendJson(response, 404, {
    error: "Not found",
    validPaths: ["/", "/health", "/calculate"]
  });
});

server.listen(port, "0.0.0.0", () => {
  console.log(`shipfast-api-node running on port ${port}`);
  console.log("Available endpoints: /, /health, /calculate");
});
