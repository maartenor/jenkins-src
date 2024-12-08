import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Calculate elapsed time in seconds
        elapsed_time = int(time.time()) // 5 * 5
        message = f'Hello World - {elapsed_time} seconds'
        
        # Send HTTP response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f'<html><body><h1>{message}</h1></body></html>', 'utf-8'))

if __name__ == '__main__':
    # Create HTTP server with custom handler
    server = HTTPServer(('0.0.0.0', 8088), RequestHandler)
    print('Starting server on port 8088...')
    server.serve_forever()