print('игра "угадай число"')
from random import randint
y=0
x=randint(0,100)
while True:
    c=int(input())
    y+=1
    if c == x:
        print('верно')
        print("совершено", y ,"попыток")
        break
    if c < x:
        print('загаданное число больше')
    else:
        print('загаданное число меньше')