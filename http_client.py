#import socket module
from socket import *
import sys

#retrienve serverName,serverPort, and filename from client
#input =  sys.argv()
serverName = sys.argv[1]
port = sys.argv[2]
serverPort = int(port)
filename = sys.argv[3]

#Create socket for communication
#AF_INET specifies address family which is IPv4
#SOCK_STREAM protocol for TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Initiate TCP connection / Three way handshake
clientSocket.connect((serverName, serverPort))

html_request = 'GET  /' + filename + ' HTTP/1.1\r\nHost: ' + serverName + '\r\n\r\n'

#send request to server
clientSocket.send(html_request.encode())

#revieve message from server
htmlresponse = clientSocket.recv(2048)

#display message
print(htmlresponse.decode())

#close socket connection
clientSocket.close()
