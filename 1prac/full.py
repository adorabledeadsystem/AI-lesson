#1.2 пример 
x = 3+5.2 * 7 
y = None 
z = 'a', 5, 12.345, (2, 'b') 
df = [['Антонова Антонина', 34, 'ж'],['Борисов Борис', 26, 'м']] 
A = {1, 'title', 2, 'content'}
print('Ответ: ', '\n', x, '|', type(x), '\n', y, '|', type(y), '\n', z, '|', type(z), '\n', df, '|', type(df), '\n', A, '|', type(A))

#1.3
x = 5 >= 2 
A = {1,3,7,8} 
B = {2,4,5,10, 'apple'} 
C = A & B 
df = 'Антонова Антонина', 34, 'ж' 
z = 'type' 
D = [1, 'title', 2, 'content'] 
print(x, '|', type(x), '\n', A, '|', type(A), '\n', B, '|', type(B), '\n', C, '|', type(C), '\n', df, '|', type(df), '\n', z, '|', type(z), '\n', D, '|', type(D), '\n')

#2.2 пример
x = 125 
if x < 0: 
    print("x отрицательный") 
elif x==0: 
    print("x равен нулю") 
else: 
    print("x положительный")
    
    
#2.3
x = 0 
if x < -5: 
    print([-infinity, -5]) 
elif x >= -5 & x <= 5: 
    print([-5, 5]) 
else: 
    print([5, +infinity])
    
    
    
 #пример 3.2.1
x = 1 
while x <= 10: 
    print(x) 
    x += 3
    
    #пример 3.2.2
models = ['KNN', 'decision tree', 'linear model'] 
for model in models: 
    print(model)
    
    
    #пример 3.2.3 
list_int = range(1,100,7) 
print(list(list_int))



#пример 3.2.4 
for i in range(5, 106, 25): 
    print(i)
    
    
    
    #пример 3.2.5 
a = [1,2,3,4,5,6,7,8,9] 
b = a[1:7:2] 
c = a[::-1] 
print(b) 
print(c)



#3.3.1
x = 10
while x >= 1: 
    print (x) 
    x -= 3

    
    
    
    #3.3.2
human = ['character', 'age', 'race']
for characteristics in human: 
    print (characteristics)
    
    
    #3.3.3
A = range(2,16,1)
print (list(A))



#3.3.4
for i in range(106, 5, -25): 
    print(i)
    
    
    
    #3.3.5
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range (0, 9, 2): 
    x[i] = len(x) - 2 - i 
print (x)



#4.2.1 пример 
import math as m 
print(m.sin(m.e))



#4.2.2 пример 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import simps 
from numpy import trapz 
x = np.arange(0.0, 10, 0.1) 
y = np.abs(np.sin(x*np.exp(np.cos(x)))) 
plt.grid() 
plt.plot(x, y, c = "r") 
plt.fill_between(x, y)
area = trapz(y) 
print(area)



#4.2.3 пример 
from matplotlib import pyplot as plt 
import numpy as np

marks = ['Неуд', 'Удовл', 'Хор', 'Отл']

data = [3, 7, 8, 4] 
fig = plt.figure(figsize = (10,7)) 
plt.pie(data, labels = marks) 
plt.show() 
plt.grid() 
plt.scatter(marks,data)



#4.3.1
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



#4.3.2
import matplotlib.pyplot as plt
import math as m

#abs - модуль
#pow - возведение в степень
#sqrt - корень

def fun(x:float) -> float:
    loga = m.log(abs(2*x))
    p1 = m.sqrt(1 + m.pow(m.e, m.sqrt(x)) + m.pow(m.cos(x), 2))
    p2 = abs(1 - m.pow(m.sin(x), 3))
    return p1/p2 + loga
mas = []

for i in range(1,11):
    mas.append(fun(i))

mas_slice = mas[0:10]
slice_fig, slice_ax = plt.subplots(figsize=(10,7))
slice_ax.scatter(x = range(0, len(mas_slice)), y = mas_slice, color = "r") 
plt.plot(range(0,10), mas)

    
plt.title("Graphic")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()



#4.3.3

import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.integrate import simps
from numpy import trapz as tr



def fun(x: float) -> float:
    return abs(m.cos(x * m.pow(m.e, m.cos(x) + m.log(x + 1, m.e))))


xs = range(0, 11, 1)
ys = []
for i in xs:
    ys.append(fun(i))

plt.plot(xs, ys, color ="r")
plt.fill_between(xs, ys)
print(tr(ys))
plt.title("Graphic")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show();



#4.3.5
import math as mh

x = float(input('Введите x: '))
y = float(input('Введите y: '))
print("+ - Выберите 1")
print("- - Выберите 2")
print("* - Выберите 3")
print("/ - Выберите 4")
print('sin - Выберите 5')
print('cos - Выберите 6')
print('x^y - Выберите 7')
print('e^(x + y) - Выберите 8')
operation = str(input('Выберите операцию: '))

if operation == "1":
    print(x + y)
elif operation == "2":
    print(x - y)
elif operation == "3":
    print(x * y)
elif operation == "4":
    if y > 0:
        print(x / y)
    else:
        print("Деление на ноль невозможно")
elif operation == '5':
    print(mh.sin(x + y))
elif operation == '6':
    print(mh.cos(x + y))
elif operation == '7':
    print(mh.pow(x, y))
elif operation == '8':
    print(mh.pow(mh.e, x + y))
else:
    print('Такой операции не существует')
