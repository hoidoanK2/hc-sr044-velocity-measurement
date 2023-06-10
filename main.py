import serial
import time

Dataserial = serial.Serial('COM3', 9600)
print(Dataserial)
time.sleep(1)

done = False

file = input("Nhập tên file: ")

i = 0
f = open(f"{file}.txt", "w")
while not done:
    
    while Dataserial.inWaiting() == 0:
        pass
    data = Dataserial.readline()
    data = str(data, 'utf-8')     
    data = data.strip('\r\n')
    print(data)
    data = data.strip('cm/s')
    data = float(data)
    f.write(f"{data}\n")
f.close() 