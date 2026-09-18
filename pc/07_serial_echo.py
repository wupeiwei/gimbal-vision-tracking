import serial
import time

ser = serial.Serial('COM5', 115200, timeout=1)

for i in range(1,6):
    msg = f"ping{i}\n"
    ser.write(msg.encode('utf-8'))
    reply = ser.readline()
    print(reply.decode().strip())
    time.sleep(1)
ser.close()
