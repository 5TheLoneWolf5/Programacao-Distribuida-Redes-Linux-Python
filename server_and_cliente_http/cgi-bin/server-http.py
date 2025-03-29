"""

Iniciar servidor HTTP com página web:

python -m http.server --cgi 8000 ---> dentro de /server_and_cliente_http

Página:

http://127.0.0.1:8000/cgi-bin/server-http.py

"""

print(
    """\
Content-Type: text/html

<!DOCTYPE html>
    <html lang="en">
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
"""
)