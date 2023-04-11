import socket
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
FILE_PATH = sys.argv[3]

# create a TCP socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# send HTTP GET request to the server
http_request = (f"GET /{FILE_PATH} HTTP/1.1\r\nHost: {SERVER_HOST}\r\n\r\n")
client_socket.sendall(http_request.encode())

# receive and display the server response
server_response = client_socket.recv(1024).decode()
print(server_response)

# close the socket
client_socket.close()