from os import system
from data import *
from helpers import *


system('CLS')
name = input("...Как тебя зовут?...\n")
player["name"] = name
system('CLS')

sleep(3)
print("...Проснись...")
sleep(3)
system('CLS')
print(f"...Проснись, {name}...")
sleep(3)
system('CLS')
print(f"{name}, наконец то ты услышал меня!")
sleep(1)
print()
print("Злой Доминик Торетто похитил принцессу и держит её в заточении!")
sleep(1)
print()
print("Нам требуется твоя помощь!")
sleep(1)
print()
print("Помоги нам спасти принцессу!")
ans = input('''1 - Хорошо
2 - не
''')
if ans == "2":
    system('CLS')
    print("...")
    sleep(1)
    print("...")
    sleep(1)
    print("Зачем ты тогда включил игру?")
    sleep(1)
    print("...")
    sleep(1)
    print("А тебя никто не спрашивал :))))")
    input("Нажмите Enter, чтобы продолжить ")
else:
    input("Нажмите Enter, чтобы продолжить ")


while True:
    if player['enemy_number'] == 6:
        print('Вы победили всех противников и спасли принцессу!')
        print('Вы прошли игру, поздравляем!')
        input('Нажмите Enter, чтобы продолжить ')
        break
    system('CLS')
    print('Выберите действие:')
    print('1 - В бой!')
    print('2 - Тренировка.')
    print('3 - Информация об игроке.')
    print('4 - Информация о противнике.')
    print('5 - Магазин.')
    print('6 - Инвентарь.')
    print('7 - Работа.')

    action = input()
    
    if action == '1':
        fight()
    elif action == '2':
        training()
    elif action == '3':
        player_info()
    elif action == '4':
        enemy_info()
    elif action == '5':
        shop()
    elif action == '6':
        inventory_info()
    elif action == '7':
        work()