
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
import ssl

context = ssl._create_unverified_context()

conn = http.client.HTTPSConnection("localhost", 4443, context=context)
conn.request("GET", "/cgi-bin/safe-server-http.py")
response = conn.getresponse()
print(response.status)
print(response.read().decode("utf-8"))