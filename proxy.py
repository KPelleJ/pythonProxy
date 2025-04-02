from socket import *
from threading import *
import restClient
import time


def start():
    serverport = 12000
    serversocket = socket(AF_INET,SOCK_DGRAM)
    
    serversocket.bind(('', serverport))
    
    print("The server is ready to receive")
    
    def handleClient(message, address):
        time.sleep(2)
        modifiedMessage = message.decode()
        restClient.post(modifiedMessage)
    
    
    while True:
        message, clientAddress = serversocket.recvfrom(2048)
        Thread(target=handleClient, args=(message, clientAddress)).start()