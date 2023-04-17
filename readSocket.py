from socket import *
import time
import struct



port = 8080
socketPc = socket(AF_INET, SOCK_DGRAM) #Socket UDP
socketPc.bind(('', port))  #Lier la socket au port
print(socketPc)
#Initialisation de la connexion
while True :
    print("waiting message...")
    message, carteAdresse = socketPc.recvfrom(2048)
    print("Message: %s"%message.decode("utf-8"))
    print("From "+str(carteAdresse))
print("end")

socketPc.close()
