from socket import *
import keyboard

port = 8080 
socketPc = socket(AF_INET, SOCK_DGRAM) #Socket UDP
socketPc.bind(('', port))  #Lier la socket au port 
i = 0
print("Waiting for ...\n")
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir un message 
print("Le message reçue  est ", message.decode("utf-8"))


"""
messagePc = "z".encode("utf-8")
socketPc.sendto(messagePc, carteAdresse) #Envoie du a 
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir une confirmation 
print("Autre message reçue : ", message.decode("utf-8"))

messagePc = "q".encode("utf-8")
socketPc.sendto(messagePc, carteAdresse) #Envoie du a 
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir une confirmation 
print("Autre message reçue : ", message.decode("utf-8"))

messagePc = "d".encode("utf-8")
socketPc.sendto(messagePc, carteAdresse) #Envoie du a 
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir une confirmation 
print("Autre message reçue : ", message.decode("utf-8"))

messagePc = "s".encode("utf-8")
socketPc.sendto(messagePc, carteAdresse) #Envoie du a 
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir une confirmation 
print("Autre message reçue : ", message.decode("utf-8"))
"""
while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        print("Touche pressée :", event.name)    
        messagePc = event.name.encode("utf-8")
        socketPc.sendto(messagePc, carteAdresse) #Envoie du a 
        #message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir une confirmation 
        #print("Autre message reçue : ", message.decode("utf-8"))


