from socket import *
import time
import struct

port = 8080
socketPc = socket(AF_INET, SOCK_DGRAM) #Socket UDP
socketPc.bind(('', port))  #Lier la socket au port

#Initialisation de la connexion
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir un message
print("Le message reçue  est ", message.decode("utf-8"))

i = 0
start = 2000 
step = 10
nbEtape = 10
#fichier pour sauvegarder les temps
f = open("carte.txt", 'w')

while i < nbEtape:
    messagePc = str(start).encode("utf-8")
    debut = time.time()
    socketPc.sendto(messagePc, carteAdresse)
    message, carteAdresse = socketPc.recvfrom(start*4) #Attendre de recevoir un message
    fin = time.time()
    #print("Le message", message)
    taille = len(message)/4
    int_array = struct.unpack('<'+str(start)+'I', message)
    print("Le ", i + 1 ," em nombre premier: ", i+1,  " ,reçue en: ", fin-debut)
    f.write(str(start) + "\t" + str(fin-debut) + "\n")
    i += 1
    start += step

f.close()
