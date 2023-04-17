import serial, time
num_captors = 2
sers = []
def getSers():
    return [serial.Serial("/dev/ttyUSB0", 115200,timeout=1), serial.Serial("/dev/ttyUSB1", 115200,timeout=1)]

def getId(ser):
    ser.write(bytes([0x5A, 0x04, 0x11, 0x01, 0x6B]))
    response = ser.read(7)
    if len(response) == 7 and response[0] == 0x5A and response[1] == 0x04 and response[2] == 0x11 and response[3] == 0x01 and response[4] == 0x5A and response[5] == 0x5A:
        id_byte = response[6]
        sensor_id = (0x55 ^ 0x04 ^ 0x00 ^ id_byte) & 0xFF
        return sensor_id
    else:
        print('Error getting ID: '+str(response))



def read_tfluna_data(ser):
    if ser.isOpen() == False:
        ser.open()

    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8 or True:
            bytes_serial = ser.read(9) # read 9 bytes
            ser.reset_input_buffer() # reset buffer

            if len(bytes_serial) == 9 and bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3] * 256 # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5] * 256
                return distance, strength


def switchInReadMode(ser):
    ser.write(bytes([0x5A, 0x05, 0x02, 0x00, 0x00, 0x00, 0x07, 0xAB]))
    
while True :
    try :
        sers = getSers()
        print("set in read mode")
        for ser in sers:
            switchInReadMode(ser)
        while (True):
            for ser in sers:
                distance, strength = read_tfluna_data(ser)
                id = getId(ser)
                print(ser.port+" ("+str(id)+") "+": "+str(distance))
            time.sleep(.2)


    except KeyboardInterrupt:
        print("closing")
        for ser in sers :
            print(ser.close())
        print("closed "+str(len(sers)))
        break

    except Exception as e:
        print(e)
        print("retryin")
        if(len(sers)==0):
            try:
                sers = getSers()
            except:
                print('cannot open serials')
        for ser in sers :
            ser.close()
