# Get your IP address:

import socket

ip = socket.gethostbyname(socket.gethostname())
print(f'My IP address is: {ip}')

# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# print(f'My IP address is: {ip}')
