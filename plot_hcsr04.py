import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy.signal import medfilt

file = input("Nhập tên file: ")

y = []
for line in open(f'{file}.txt', 'r'):
    y.append(float(line))
z = y
median_value = statistics.median(y)

for i in range(0,len(y)):
    if abs(y[i]) > 30*abs(median_value):
        y[i] = median_value
    else:
        continue


y = np.array(y)
y = medfilt(y, 3)
x = np.arange(len(y))


plt.subplot(2,1,1)
plt.plot(x,z,'yo-')
plt.title('input signal')
plt.xlabel('time')
plt.subplot(2,1,2)
plt.plot(x,y,'yo-')
plt.title('filtered signal')
plt.xlabel('time')
plt.show()