import socket
import threading


def handle_connection(client_connection):
    while True:
        try:
            client_connection.recv(1024)  # wait for client to send data
            client_connection.send(b"+PONG\r\n")
        except ConnectionError:
            break  # Stop serving if the client connection is closed


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client, _ = server_socket.accept()  # wait for client
        threading.Thread(target=handle_connection, args=(client,)).start()
     

if __name__ == "__main__":
    main()
