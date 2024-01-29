import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).deode('utf-8')
            if not message:
                break
            print(f"Received from {address[0]}:{address[1]}: {message}")

            broadcast(message,client_socket)
        except ConnectionResetError:
            break
    print(f"Connection with {address[0]}:{address[1]} closed.")
    client_sockets.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in client_socket:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except ConnectionResetError:
                continue

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)

    print("Server listing on port 12345...")

    while True:
        client_socket, address = server_socket.accept()
        print(F"Accepted connection from {address[0]}:{address[1]}")

        client_socket.append(client_socket)
        client_thread = threading.Thread(target=handling_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    client_sockets = []
    start_server()
