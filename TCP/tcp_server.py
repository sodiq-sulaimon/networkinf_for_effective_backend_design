import socket

def start_tcp_server(host='localhost', port=8500):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        connection, address = server_socket.accept()
        with connection:
            print(f"Connected by {address}")
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                connection.sendall(data)  # Echo the received data back to the client

if __name__ == "__main__":
    start_tcp_server()
