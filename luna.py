import serial, time, socket, sys
import numpy as np

port = 8080
addr = ("169.254.23.214", port)

ser = serial.Serial("/dev/serial0", 115200,timeout=0) # mini UART serial device
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

socketPc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Socket UDP
socketPc.bind(('', port))  #Lier la socket au port
print("Waiting for ...\n")
message, carteAdresse = socketPc.recvfrom(2048) #Attendre de recevoir un message
print("Le message reçue  est ", message.decode("utf-8"))
print(carteAdresse)
addr = carteAdresse
def read_tfluna_data():
    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9) # read 9 bytes
            ser.reset_input_buffer() # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256 # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256 # signal strength in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256 # temp in next two bytes
                temperature = (temperature/8.0) - 256.0 # temp scaling and offset
                return distance/100.0,strength,temperature

if ser.isOpen() == False:
    ser.open() # open serial port if not open


client_socket.sendto(b'z', addr)
client_socket.sendto(b'z', addr)
client_socket.sendto(b'z', addr)
client_socket.sendto(b'z', addr)

stopped = False

while (True):
    try :
        time.sleep(0.2)
        distance,strength,temperature = read_tfluna_data()
        print(distance)
        if stopped:
            client_socket.sendto(b'z', addr)
            client_socket.sendto(b'z', addr)
            client_socket.sendto(b'z', addr)
            client_socket.sendto(b'z', addr)
            stopped = False
        if(distance<0.1):
            client_socket.sendto(b's', addr)
            # client_socket.sendto(b'q', addr)
            stopped = True





    except KeyboardInterrupt:
        ser.close() # close serial port
        break


ser.close() # close serial port
