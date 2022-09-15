#4.3
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
plt.fill_between(xs, ys) #вставить между
print(tr(ys))
plt.title("Graphic")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show();
