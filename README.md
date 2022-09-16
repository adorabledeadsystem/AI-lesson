x = 5 >= 2
A = {1,3,7,8}
B = {2,4,5,10, 'apple'}
C = A & B
df = 'Антонова Антонина', 34, 'ж'
z = 'type'
D = [1, 'title', 2, 'content']
print(x, '|', type(x), '\n', A, '|', type(A), '\n', B, '|', type(B), '\n', C, '|', type(C), '\n', df, '|', type(df), '\n', z, '|', type(z), '\n', D, '|', type(D), '\n')



x = 0 
if x < -5:
    print([-infinity, -5])
elif x >= -5 & x <= 5:
    print([-5, 5])
else:
    print([5, +infinity])
    
    
    
    x = 10
while x >= 1:
    print (x)
    x -= 3
    
    
    
    human = ['character', 'age', 'race']
for characteristics in human: 
    print (characteristics)
    
    
    
    
    A = range(2,16,1)
print (list(A))




for i in range(106, 5, -25):
    print(i)
    
    
    
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range (0, 9, 2):
    x[i] = len(x) - 2 - i
print (x)


    
    
    
    
    import numpy as np
import statistics 
import matplotlib.pyplot as plt

a = np.random.rand(5)
medium = statistics.mean(a)
mediana = statistics.median(a)
print(a)
print(medium)
print(mediana)

plot = plt.scatter(medium, mediana)
plt.show()






#1 пример
x = 3+5.2 * 7
y = None
z = 'a', 5, 12.345, (2, 'b')
df = [['Антонова Антонина', 34, 'ж'],['Борисов Борис', 26, 'м']]
A = {1, 'title', 2, 'content'}

print('Ответ: ', '\n', x, '|', type(x), '\n', y, '|', type(y), '\n',
      z, '|', type(z), '\n', df, '|', type(df), '\n', A, '|', type(A))
      
      
      #2 пример
x = 125
if x < 0:
    print("x отрицательный")
elif x==0:
    print("x равен нулю")
else:
    print("x положительный")
    
    
    #пример 3.1
x = 1
while x <= 10:
    print(x)
    x += 3
    
    
    
    
    #пример 3.2
models = ['KNN', 'decision tree', 'linear model']
for model in models:
    print(model)


#пример 3.3
list_int = range(1,100,7)
print(list(list_int))

#пример 3.4
for i in range(5, 106, 25):
    print(i)

#пример 3.5
a = [1,2,3,4,5,6,7,8,9]
b = a[1:7:2]
c = a[::-1]
print(b)
print(c)

#4.1 пример
import math as m
print(m.sin(m.e))

#4.2 пример
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

#4.3 пример
from matplotlib import pyplot as plt
import numpy as np

marks = ['Неуд', 'Удовл', 'Хор', 'Отл']

data = [3, 7, 8, 4]
fig = plt.figure(figsize = (10,7))
plt.pie(data, labels = marks)
plt.show()
plt.grid()
plt.scatter(marks,data)
