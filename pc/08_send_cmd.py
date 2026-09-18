import sys
import serial

if len(sys.argv) < 2:
    print('用法: python 08_send_cmd.py "led on"')
    sys.exit(1)

cmd = sys.argv[1]

ser = serial.Serial('COM5', 115200, timeout=1)
ser.write((cmd + '\n').encode('utf-8'))   

reply = None
for _ in range(5):                       
    line = ser.readline()
    if line == b'':                      
        break
    text = line.decode().strip()
    if text == 'oh':                     
        continue
    
    reply = text                         
    break

if reply is None:
    print('超时：没等到应答')
else:
    print('应答:', reply)

ser.close()