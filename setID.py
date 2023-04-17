import serial
sers = [serial.Serial("/dev/ttyUSB0", 115200,timeout=1), serial.Serial("/dev/ttyUSB1", 115200,timeout=1)]


def set_id(ser, id_value):
    #set in idle mode
    ser.write(bytes([0x42, 0x57, 0x02, 0x00, 0x00, 0x00, 0x41]))
    print(ser.port+' '+str(id_value))
    id_bytes = id_value.to_bytes(4, byteorder='little')
    parity_byte = (0x55 ^ 0x05 ^ 0x00 ^ 0x5A ^ id_bytes[0] ^ id_bytes[1] ^ id_bytes[2] ^ id_bytes[3]) & 0xFF
    command = bytes([0x55, 0x04, 0x00, 0x01]) + id_bytes + bytes([parity_byte])
    ser.write(command)
    response = ser.read(4)
    print(f"Command: {command}")
    print(f"Response: {response}")
    if response == b'YY\x00\x00\x00':
        print(f"Successfully set ID to {id_value}")
    else:
        print(f"Error setting ID for TFLuna sensor on {ser.name}")

# Assign a unique ID to each TFLuna sensor
for i in range(len(sers)):
    set_id(sers[i], 10+i)

print("closing")
for ser in sers :
    print(ser.close())
print("closed "+str(len(sers)))
