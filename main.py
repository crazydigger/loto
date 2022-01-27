import random


class Player:

    def __init__(self, cells, n):
        # карточка игрока

        self.card = []
        # имя игрока
        self.name = n
        # победитель?
        self.winner = True

        for j in range(3):
            for i in range(cells):
                self.card.append(str(random.randint(0, 100)))

    def close(self, num):
        card_temp = []
        for c in self.card:
            if c == str(num):
                print('found', num)
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

    def iswinner(self):
        self.winner = True
        for c in self.card:
            if c != '--':
                self.winner = False
                return self.winner


# число игроков
# бочки
markers = []
for i in range(90):
    markers.append(str(random.randint(0, 100)))
    print(markers)
num = input('введите число игроков 0- 2:')
while int(num) <= 2:
    players = []
    for i in range(int(num)):
        name = input('введите имя игрока' + str(i) + 'или <comp>если играет компьютер')
    print('минимальное количество - 2 игрока!')

    p = Player(5, name)
    players.append((p))
    p.show()
    count = 0
    all = len(markers)
    for m in markers:
        count = count+1
        print('бочка номер', m, count, 'from', all)
    for p in players:

        p.show()
        num = input('какую цифру закрыть:') or m

        p.close(int(num))
        print(m, p.name,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        p.show()
if p.iswinner():
    print('победил игрок!!!!!!!!!!!!!!!!!!!!!!!!!!!!', p.name)

    print('введена некорректная цифра')
    p.show()
    if name == 'comp':
        print(name)

        for m in Markers:
            print('бочка номер', m)
            for p in Players:
                print('игрок', p.name)
                num = input('какую цифру закрыть?')
                if p.name == 'comp':
                    p.close(int(m))
                p.close(int(num))

                p.show()
