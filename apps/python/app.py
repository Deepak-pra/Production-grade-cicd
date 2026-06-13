"""
shipfast-api-python
Small HTTP runtime used for GitHub Actions CD deployment demo.
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from calculator import add, divide, multiply, subtract
from pipeline import calculate_average, calculate_discount, calculate_total, is_bulk_order


class ShipfastHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, payload):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send_json(
                200,
                {
                    "service": "shipfast-api-python",
                    "status": "running",
                    "message": "Python artifact deployed successfully",
                },
            )
            return

        if self.path == "/health":
            self._send_json(
                200,
                {
                    "service": "shipfast-api-python",
                    "status": "healthy",
                },
            )
            return

        if self.path == "/calculate":
            self._send_json(
                200,
                {
                    "add": add(10, 5),
                    "subtract": subtract(10, 5),
                    "multiply": multiply(10, 5),
                    "divide": divide(10, 5),
                    "discount": calculate_discount(100, 10),
                    "total": calculate_total([10, 20, 30]),
                    "average": calculate_average([10, 20, 30]),
                    "bulk_order": is_bulk_order(15),
                },
            )
            return

        self._send_json(
            404,
            {
                "error": "Not found",
                "valid_paths": ["/", "/health", "/calculate"],
            },
        )

    def log_message(self, format, *args):
        return


def main():
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), ShipfastHandler)

    print(f"shipfast-api-python running on port {port}")
    print("Available endpoints: /, /health, /calculate")

    server.serve_forever()


if __name__ == "__main__":
    main()