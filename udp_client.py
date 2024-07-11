import socket

# Define server address and port
server_address = ('localhost', 5500)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send data
    message = b'Hey there! This is a test message from Sodiq.'
    print('Sending:', message.decode())
    sent = client_socket.sendto(message, server_address)

    # Receive response
    data, server = client_socket.recvfrom(1024)
    print('Received:', data.decode())
finally:
    print('Closing socket')
    client_socket.close()
