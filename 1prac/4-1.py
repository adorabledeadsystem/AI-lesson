import random
import math as m
import numpy as np
import matplotlib.pyplot as plt
list = []
for i in range(0, 21):
    list.append(random.randint(0, 100) / 100)
xAxis = []
for i in range(0, 21):
    xAxis.append(i)
sortedList = sorted(list)
median = 0
if len(sortedList) % 2 == 0:
    median = (sortedList[len(sortedList) // 2] + sortedList[len(sortedList) // 2 - 1]) / 2
else:
    median = sortedList[len(sortedList) // 2 - 1]
median = round(median, 2)
mid = round(sum(list) / len(list), 2)
print('list = ', list)
print('median = ', median)
print('mid = ', mid)
colors = np.random.uniform(15, 86, len(xAxis))
plt.grid()
plt.scatter(xAxis, list, 30, colors, vmin=0, vmax=100)
plt.show()
