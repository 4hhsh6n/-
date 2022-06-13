from copy import error
from random import randint

game = True
num = randint(1, 100)


print('Попробуй угадай число от 1 до 100')


while game:
    x = input('Ваше предположение: ')
    x = int(x)
    if x > num:
        print(f'Попробуйте число меньше {x}')
    elif x < num:
        print(f'Попробуйте число больше {x}')
    if x == num:
        print('Вы угадали верно!')
        break


