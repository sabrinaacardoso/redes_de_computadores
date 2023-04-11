# Import socket module
from socket import *
# Import thread module
from threading import Thread
# In order to terminate the program
import sys

class MultiThreadServer(Thread):

    def __init__(self, connect, address):
        Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        print ("Run Multithread Server . . . ")
        while 1:
            #Establish the connection
            print('Ready to serve...')
            try:
                message = self.connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                print(outputdata)
                self.connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

                for i in range(0, len(outputdata)):
                    self.connectionSocket.send(outputdata[i].encode())

            except IOError:
                print('entrando pro except')
                self.connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n404 Not Found".encode())      

if __name__=='__main__':

    serverPort = 6789      # The port used by the server
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', serverPort))
    serverSocket.listen(30)

    while 1:
        print("Server ready to recive!")
        connectionSocket, addr = serverSocket.accept()
        print("Address:\n", addr)
         
        client_thread = MultiThreadServer(connectionSocket, addr)
        client_thread.start()

    serverSocket.close()
    sys.exit()