#4.5
import math as m

print('e^(x + y) => a')
print('sin(x + y) => b')
print('cos(x+y) => c')
print('x^y => d')

x = float(input('Enter x: '))
y = float(input('Enter y: '))
op = str(input('Enter operation: '))

if op == 'Сумма' or op == 'сумма':
    print(x + y)
elif op == 'Вычитание' or op == 'вычитание':
    print(x - y)
elif op == 'Умножение' or op == 'умножение':
    print(x * y)
elif op == 'Деление' or 'деление':
    print(x / y)
elif op == 'a':
    print(m.pow(m.e, x + y))
elif op == 'b':
    print(m.sin(x + y))
elif op == 'c':
    print(m.cos(x + y))
elif op == 'd':
    print(m.pow(x, y))
else:
    print('Invalid operation')
