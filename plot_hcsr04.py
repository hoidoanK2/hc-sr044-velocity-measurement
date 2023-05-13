import matplotlib.pyplot as plt

file = input("Nhập tên file: ")
x = []
y = []
for line in open(f'{file}.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(float(lines[1]))
      
# plt.title("")
# plt.xlabel('')
# plt.ylabel('')
plt.yticks(y)
plt.plot(x, y, c = 'b')
plt.show()