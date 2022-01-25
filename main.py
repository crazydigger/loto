# число игроков
num = input('введите число игроков:')
while int(num) <= 2:

    print('минимальное количество - 2 игрока!')
    players = []
    for i in range(int(num)):
        name = input('введите имя игрока' + str(i) + 'или <comp>если играет компьютер')
        players.append((name))
    if name == 'comp':
        print(name)
        break
