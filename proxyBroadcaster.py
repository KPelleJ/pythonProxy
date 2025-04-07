from socket import *
import time
import randomAnimal
import json

serverName = '127.0.0.255'
serverPort = 12000


def broadCast():
     while True:
          clientSocket = socket(AF_INET, SOCK_DGRAM)
          clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

          animalToAdd = randomAnimal.randomAnimal()
          message = json.dumps(animalToAdd)
          clientSocket.sendto(message.encode(), (serverName, serverPort))

          clientSocket.close()
          print(f"New animal: {message} has been sent")
          time.sleep(15)