import ssl

hostname = "google.com"
port = 443
certificate = ssl.get_server_certificate((hostname, port))
print(certificate)