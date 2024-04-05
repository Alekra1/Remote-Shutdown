import http.server
import socketserver
import threading
import subprocess


class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Server Running</h1></body></html>')

        # Shutdown the computer
        subprocess.run(['shutdown', '/s', '/f', '/t', '0'])


def start_server(port):
    handler = HTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server started on port", port)
        httpd.serve_forever()


if __name__ == "__main__":
    port = 8080  # Change this to the desired port number
    server_thread = threading.Thread(target=start_server, args=(port,))
    server_thread.start()
