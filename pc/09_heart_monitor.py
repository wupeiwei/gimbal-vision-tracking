import serial
import time

DURATION = 5                     

ser = serial.Serial('COM5', 115200, timeout=1)

t0 = time.time()                 
count = 0

print(f'开始监视 {DURATION} 秒……')

while time.time() - t0 < DURATION:     
    line = ser.readline()
    if line == b'':                    
        continue
    text = line.decode().strip()
    if text == 'oh':
        count += 1
        print(f'[{time.time() - t0:5.1f}s] 心跳 #{count}')
    else:
        print(f'[{time.time() - t0:5.1f}s] 其他: {text}')

if count > 0:
    print(f'平均间隔: {DURATION * 1000 / count:.0f} ms')
print(f'结果：{DURATION} 秒内收到 {count} 条心跳')

ser.close()