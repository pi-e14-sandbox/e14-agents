import unittest

import app


class RouteTest(unittest.TestCase):
    def test_routes_of_the_contract(self):
        self.assertEqual(app.route('GET', '/api/orders'), ('list_orders', ()))
        self.assertEqual(app.route('GET', '/api/orders/7'), ('get_order', ('7',)))
        self.assertEqual(app.route('GET', '/api/customers/c1'), ('get_customer', ('c1',)))
        self.assertEqual(app.route('DELETE', '/api/orders/7'), (None, ()))

    def test_create_order(self):
        order = app.create_order({'customerId': 'c1', 'totalCents': 250})
        self.assertEqual(order['totalCents'], 250)


if __name__ == '__main__':
    unittest.main()
