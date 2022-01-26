import random
class Player:

    def __init__(self, cells, n):
        #карточка игрока

        self.card = []
        #имя игрока
        self.name = n
        for i in range(cells):
            self.card.append(random.randint(0,99))
    def show(self):
        print('игрок:', self.name)
        for c in self.card:

            print(c)
# число игроков
num = input('введите число игроков:')
while int(num) <= 2:

    print('минимальное количество - 2 игрока!')
    players = []
    for i in range(int(num)):
        name = input('введите имя игрока' + str(i) + 'или <comp>если играет компьютер')
        p = Player(15,name)
        players.append((p))
        p.show()
    if name == 'comp':
        print(name)
        break
