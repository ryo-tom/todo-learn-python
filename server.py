from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# TODO: jsonファイルの読み込み


class TodoHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, content=None):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if content:
            self.wfile.write(json.dumps(content).encode())

    def do_GET(self):
        self._send_response(200, {'message': 'Server is running'})


def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TodoHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
