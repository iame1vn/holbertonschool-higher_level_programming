from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # /data endpoint → JSON response
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        
        # /status endpoint → API status
        elif self.path == "/status":
            status_data = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(status_data).encode())
        
        # Undefined endpoint → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
