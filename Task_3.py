'''
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

def found_quarter(x,y):
    if x > 0 and y > 0:
        print('First quarter')
    elif x < 0 and y > 0:
        print('Second quarter')
    elif x < 0 and y < 0:
        print('Third quarter')
    else:
        print('Fourth quarter')

x = int(input('Введите "X": '))
y = int(input('Введите "Y": '))

found_quarter(x,y)
