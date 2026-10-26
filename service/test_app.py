import json
import threading
import unittest
import urllib.request
from http.server import HTTPServer

import app


class RouteTest(unittest.TestCase):
    def test_routes_of_the_contract(self):
        self.assertEqual(app.route('GET', '/api/orders'), ('list_orders', ()))
        self.assertEqual(app.route('GET', '/api/orders/7'), ('get_order', ('7',)))
        self.assertEqual(app.route('GET', '/api/customers/c1'), ('get_customer', ('c1',)))
        self.assertEqual(app.route('DELETE', '/api/orders/7'), (None, ()))

    def test_health_route(self):
        self.assertEqual(app.route('GET', '/api/health'), ('health', ()))
        self.assertEqual(app.route('POST', '/api/health'), (None, ()))

    def test_health_response(self):
        server = HTTPServer(('127.0.0.1', 0), app.Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            with urllib.request.urlopen('http://127.0.0.1:%d/api/health' % server.server_port) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(json.loads(response.read()), {'ok': True})
        finally:
            server.shutdown()
            server.server_close()

    def test_create_order(self):
        order = app.create_order({'customerId': 'c1', 'totalCents': 250})
        self.assertEqual(order['totalCents'], 250)


if __name__ == '__main__':
    unittest.main()
