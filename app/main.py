import socket


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4000), reuse_port=True)
    client, _ = server_socket.accept()
    client.recv(1024)
    client.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
