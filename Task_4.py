'''
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

def find_parametres_of_quarter(n):
    if n == 1:
        print('X > 0; Y > 0')
    elif n == 2:
        print('X < 0; Y > 0')
    elif n ==3:
        print('X < 0; Y < 0')
    elif n == 4:
        print('X > 0; Y < 0')
    else:
        print(f'Параметров для четверти "{n}" не предусмотрено')


number_of_quarter = int(input('Введите номер четверти '))
find_parametres_of_quarter(number_of_quarter)