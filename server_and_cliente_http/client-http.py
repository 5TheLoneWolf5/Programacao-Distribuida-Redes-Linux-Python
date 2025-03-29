
"""

Resultado:

200
<!DOCTYPE html>
    <html lang="en">
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>

"""

import http.client

conn = http.client.HTTPConnection("127.0.0.1", 8000)
conn.request("GET", "/cgi-bin/server-http.py")
response = conn.getresponse()
print(response.status)
print(response.read().decode("utf-8"))