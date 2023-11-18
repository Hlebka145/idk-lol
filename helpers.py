from time import sleep
from random import randint
from os import system
from data import *

def fight():
    system('CLS')
    enemy_number = player['enemy_number']
    player['hp'] = player['max_hp']
    current_enemy = enemies[enemy_number]
    enemy_hp = current_enemy['hp']
    print(f'Противник - {current_enemy["name"]}.\n')
    print(f'{current_enemy["script"]}\n')
    input('Нажмите Enter, чтобы продолжить ')
    system('CLS')

    turn = randint(0, 1)

    while player['hp'] > 0 and enemy_hp > 0:
        if turn % 2 == 0: # Ход игрока
            crit_k = 1
            crit = randint(1, 100)
            if crit <= player['luck']:
                crit_k = 2
                print('Выпал крит!')
            result_damage = player['attack'] * crit_k * (1 - (current_enemy["armor"]/100))
            sleep(1)
                
            enemy_hp -= result_damage
            print(f'{player["name"]} атакует {current_enemy["name"]}!')
            sleep(1)
            print(f'{player["name"]} нанес {current_enemy["name"]} {result_damage} урона!')
        else: # Ход врага
            result_damage = current_enemy['attack'] * (1 - (player["armor"]/100))

            player['hp'] -= result_damage
            print(f'{current_enemy["name"]} атакует {player["name"]}!')
            sleep(1)
            print(f'{current_enemy["name"]} нанес {player["name"]} {result_damage} урона!')
        turn += 1
        print(f'\n{player["name"]} - {player["hp"]} хп.')
        print(f'{current_enemy["name"]} - {enemy_hp} хп.\n')
        sleep(1)
        system('CLS')

    if player['hp'] > 0:
        print(f'Противник - {current_enemy["name"]}: {current_enemy["win"]}')
        player['enemy_number'] += 1
    else:
        print(f'Противник - {current_enemy["name"]}: {current_enemy["lose"]}')
    print()
    input('Нажмите Enter, чтобы продолжить ')

def training():
    system('CLS')
    print('Выберите действие:')
    print('1. Тренировать силу.')
    print('2. Тренировать выносливость.')
    print()
    action = input()
    system('CLS')
    print('''Хотите ли вы использовать пропуск?
                 1 - Да
                 2 - Нет''')
    ans = input()
    if ans == "1":
        if "Пропуск тренировки" in player['inventory']:
            system('CLS')
            print('Вы использовали пропуск')
            player['inventory'].remove('Пропуск тренировки')
        else:
            print("У вас нет пропуска")
            print()
            system('CLS')
            for i in range(0, 101, 20):
                sleep(1.5)
                print(f'Тренировка завершена на {i}%')
    else:
        for i in range(0, 101, 20):
                sleep(1.5)
                print(f'Тренировка завершена на {i}%')
    
    if action == '1':
        player['attack'] += 5
        print("Сила увеличена на 5!")
    elif action == '2':
        player['max_hp'] += 5
        player['hp'] += 5
        print("Здоровье увеличено на 5!")
    print()
    input('Нажмите Enter, чтобы продолжить ')

def player_info():
    system('CLS')
    print(f'{player["name"]}.')
    print(f'\tАтака - {player["attack"]}.')
    print(f'\tХп - {player["hp"]}/{player["max_hp"]}.')
    print(f'\tБроня поглощает {player["armor"]}% урона.')
    print(f'\tШанс критического урона - {player["luck"]}%.')
    print(f'\tМонет - {player["money"]}.')
    print()
    input('Нажмите Enter, чтобы продолжить ')

def enemy_info():
    current_enemy = enemies[player['enemy_number']]
    system('CLS')
    print(f'{current_enemy["name"]}.')
    print(f'\tАтака - {current_enemy["attack"]}.')
    print(f'\tХп - {current_enemy["hp"]}.')
    print(f'\tБроня - {current_enemy["armor"]}.')
    print()
    input('Нажмите Enter, чтобы продолжить ')

def shop():
    system('CLS')
    print("Приветствуем вас")
    print(f"Количество моенет - {player['money']}")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")
    item = input('Введите номер вещи или "q", чтобы выйти: ')
    if item != "q":
        if player['money'] >= items[item]['price']:
            system('CLS')
            print(f"Вы успешно купили {items[item]['name']}")
            player['inventory'].append(items[item]['name'])
            player['money'] -= items[item]['price']
        else:
            print("Не хватает денег")
    print("Пока")
    input('Нажмите Enter, чтобы продолжить ')

def inventory_info():
    system('CLS')
    print('У вас есть:')
    for key, value in player['inventory']:
        print(f"{key} - {value}")
    use = input('''Хотите ли вы использовать какую-нибудь вещь из своего инвентаря?
    1 - Да
    2 - Нет''')
    if use == '1':
        use_inventory()

def use_inventory():
    system('CLS')
    use_item = input('Введите название предмета для использования: ')
    if use_item in player['inventory']:
        if use_item == 'Зелье удачи':
            potion = input(''' Выпить?
                           1 - Да
                           2- Нет: ''')
            if potion == '1':
                player['luck'] += 7
                player['inventory'].remove('Зелье удачи')
                print("Ваша удача увеличена на 7!")

        elif use_item == 'Зелье силы':
            potion = input(''' Выпить?
                           1 - Да
                           2- Нет: ''')
            if potion == '1':
                player['attack'] += 20
                player['inventory'].remove('Зелье силы')
                print("Ваша атака увеличена на 20!")
        elif use_item == 'Зелье здоровья':
            potion = input(''' Выпить?
                           1 - Да
                           2- Нет: ''')
            if potion == '1':
                player['hp'] = player['max_hp']
                player['inventory'].remove('Зелье здоровья')
                print("Ваше здоровье восстановлено!")

def work():
    system('CLS')
    print("Добро пожаловать на работу!")
    print("Каждый раз вы получаете по 100 монет")
    work = input('Нажмите Enter, чтобы начать работать или "q", чтобы выйти: ')
    if work != 'q':
        system('CLS')
        for i in range(0, 101, 20):
            sleep(1.5)
            print(f'{i}%')
        player['money'] += 100
