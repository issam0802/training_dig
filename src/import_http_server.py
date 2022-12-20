import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('http://127.0.0.1', 8000)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()
