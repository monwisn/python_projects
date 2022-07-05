# Microport scanner - web servers work on port 80 for http - unencrypted connection,
# and port 443 for https - encrypted connection.
# Checking all ip addresses on my network.
# checking what services on ip addresses are enabled: in this case, is the http server enabled,

import socket
import ipaddress


# if the answer is 0 when trying to connect, it means that the port is open,
# answer other than 0, then the port is closed.
# We can check the IP address of our network in cmd by entering the command: ipconfig.

def is_port_open(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0


ports = [
    80,
    443]

for ip in ipaddress.ip_network('192.168.0.0/24'):
    print(f"Check ip address {ip}")

    for port in ports:
        if is_port_open(str(ip), port):
            print(f'The IP {ip} address has an open port {port}')
