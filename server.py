from http.server import BaseHTTPRequestHandler, HTTPServer
import json

TODOS_FILE = "todos.json"


def load_todos():
    try:
        with open(TODOS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open(TODOS_FILE, 'w') as file:
        json.dump(todos, file)


class TodoHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, content=None):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if content:
            self.wfile.write(json.dumps(content).encode())

    def do_GET(self):
        if self.path == "/todos":
            todos = load_todos()
            self._send_response(200, todos)
        else:
            self._send_response(404, {"error": "Not Found"})

    def do_POST(self):
        if self.path == "/todos":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                todo = json.loads(post_data)

                # Validation
                if 'title' not in todo or 'completed' not in todo:
                    self._send_response(400, {'error': 'Missing required fields'})
                    return

                todos = load_todos()

                # ID自動生成
                todo['id'] = max((item['id'] for item in todos), default=-1) + 1
                todos.append(todo)
                save_todos(todos)
                self._send_response(201, todo)
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid Json"})
        else:
            self._send_response(404, {"error": "Not Found"})


def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TodoHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
