import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
target = input('Digite o alvo do scan: ')
 
target_ip = socket.gethostbyname(target)
print('Escaneando:', target_ip)
 
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
 
for port in range(65_535):
    if port_scan(port):
        print(f'Porta {port} aberta.')
    else:
        print(f'Porta {port} fechada.')