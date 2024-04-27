from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Override the do_GET method to serve HTML files without including HTML tags
    def do_GET(self):
        # Set the content type header
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # Set caching headers (Cache-Control: public, max-age=300)
        self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        # Call the parent class method to serve the requested file
        return SimpleHTTPRequestHandler.do_GET(self)

# Define the server address and port
HOST = '127.0.0.1'
PORT = 9000

# Set the directory from which to serve files
os.chdir("static")

# Create and start the HTTP server with the custom request handler
with HTTPServer((HOST, PORT), CustomHTTPRequestHandler) as server:
    print(f"Server listening on {HOST}:{PORT}")
    # Start the server
    server.serve_forever()

