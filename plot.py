import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('New.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Read from the File!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph using readfile')
plt.legend()
plt.show()