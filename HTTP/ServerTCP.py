#import socket module
from socket import *
# In order to terminate the program
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8081        # The port used by the server
serverSocket.bind(('', serverPort))
serverSocket.listen(30)
print ("Servidor pronto para receber!")

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = message =connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print (outputdata)
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()
        break
serverSocket.close()
sys.exit()