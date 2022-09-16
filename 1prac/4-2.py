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
    
plt.plot(list(range(1, 11)), mas)
    
plt.title("Graphic")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

mas_slice = mas[0:5]
slice_fig, slice_ax = plt.subplots(figsize=(12,8))
slice_ax.scatter(x = list(range(0, len(mas_slice))), y = mas_slice)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show();




import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.integrate import simps
from numpy import trapz as tr


def fun(x: float) -> float:
    return abs(m.cos(x * m.pow(m.e, m.cos(x) + m.log(x + 1, m.e))))


xs = list(range(0, 11, 1))
ys = []
for i in xs:
    ys.append(fun(i))

plt.plot(xs, ys)
plt.fill_between(xs, ys)
print(tr(ys))
plt.title("Graphic")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show();
