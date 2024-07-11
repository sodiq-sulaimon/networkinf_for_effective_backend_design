

import socket

# Define server address and port
server_address = ('localhost', 5500)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind(server_address)

print('UDP server up and listening')

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    data, client_address = server_socket.recvfrom(1024)

    print('Received {} bytes from {}'.format(len(data), client_address))
    print('Data:', data.decode())

    if data:
        # Send data back to the client
        sent = server_socket.sendto(data, client_address)
        print('Sent {} bytes back to {}'.format(sent, client_address))
