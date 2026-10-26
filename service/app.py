"""The orders service: an in-memory store behind the routes of openapi.yaml (standard library only)."""
import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

ORDERS = {}
ROUTES = [('GET', r'^/api/orders$', 'list_orders'), ('POST', r'^/api/orders$', 'create_order'), ('GET', r'^/api/orders/([^/]+)$', 'get_order'), ('GET', r'^/api/customers/([^/]+)$', 'get_customer')]


def route(method, path):
    """The handler name and path arguments of a request, or (None, ()) when no route matches."""
    for verb, pattern, name in ROUTES:
        found = re.match(pattern, path)
        if verb == method and found:
            return name, found.groups()
    return None, ()


def create_order(body):
    order = {'id': str(len(ORDERS) + 1), 'customerId': str(body['customerId']), 'totalCents': int(body['totalCents'])}
    ORDERS[order['id']] = order
    return order


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        name, args = route('GET', self.path)
        if name == 'list_orders':
            return self._send(200, list(ORDERS.values()))
        if name == 'get_order' and args[0] in ORDERS:
            return self._send(200, ORDERS[args[0]])
        if name == 'get_customer':
            return self._send(200, {'id': args[0], 'name': 'Customer ' + args[0]})
        return self._send(404, {'error': 'not_found'})

    def do_POST(self):
        name, _ = route('POST', self.path)
        if name != 'create_order':
            return self._send(404, {'error': 'not_found'})
        length = int(self.headers.get('content-length', '0'))
        return self._send(201, create_order(json.loads(self.rfile.read(length) or b"{}")))


if __name__ == '__main__':
    HTTPServer(('127.0.0.1', 8080), Handler).serve_forever()
