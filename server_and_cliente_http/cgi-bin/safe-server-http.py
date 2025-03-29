import http.server
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content="""
<!DOCTYPE html>\n\
    <html lang="en">\n\
    <body>\n\
        <h1>Hello, World!</h1>\n\
    </body>\n\
</html>\n\
"""
        encoded = content.encode("utf-8")
        self.wfile.write(encoded)
        self.wfile.flush()

httpd = http.server.HTTPServer(("localhost", 4443), Handler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.load_cert_chain(certfile='server.pem')

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True,
)

httpd.serve_forever()