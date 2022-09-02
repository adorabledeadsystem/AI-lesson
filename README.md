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
