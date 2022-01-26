import random


class Player:

    def __init__(self, cells, n):
        # карточка игрока

        self.card = []
        # имя игрока
        self.name = n
        for j in range(3):
            for i in range(cells):
                self.card.append(str(random.randint(0, 100)))

    def close(self, num):
        card_temp = []
        for c in self.card:
            if c == str(num):
                card_temp.append('--')
            else:
                card_temp.append(c)
        self.card = card_temp

    def show(self):
        print('игрок:', self.name)
        for j in range(3):
            line = ''
            for c in self.card:
                line = line + '!' + c + '!'
            print(line)


# число игроков
num = input('введите число игроков:')
while int(num) <= 2:

    print('минимальное количество - 2 игрока!')
    players = []
    for i in range(int(num)):
        name = input('введите имя игрока' + str(i) + 'или <comp>если играет компьютер')
        p = Player(5, name)
        players.append((p))
        p.show()
        num = input('какую цифру закрыть?')
        p.close(int(num))
        p.show()
    if name == 'comp':
        print(name)
        break
