import serial
import time

# Connect to Serial
Dataserial = serial.Serial('COM3', 9600)
print(Dataserial)
time.sleep(1)
done = False

# Đặt tên file
file = input("Đặt tên file: ")

i = 0
f = open(f"{file}.txt", "w")
while not done:
    """
    Viết data vận tốc vào 1 file text
    """
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
