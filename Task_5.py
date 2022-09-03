'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
import math


def find_distance(dot_1_x, dot_1_y, dot_2_x, dot_2_y):
    distance = math.sqrt((dot_2_x - dot_1_x)**2 + (dot_2_y - dot_1_y)**2)
    print(round(distance, 3))


xa= float(input('Введите X координату первой точки: '))
ya = float(input('Введите Y координату первой точки: '))
xb= float(input('Введите X координату второй точки: '))
yb = float(input('Введите Y координату второй точки: '))

find_distance(xa,ya, xb, yb )
