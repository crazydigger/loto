import random


class Player:

    def __init__(self, cells, n):
        # карточка игрока

        self.card = []
        # имя игрока
        self.name = n
        # победитель?
        self.winner = False

        for j in range(3):
            for i in range(cells):
                self.card.append(str(random.randint(0, 100)))

    def close(self, num):
        card_temp = []
        for c in self.card:
            if c == str(num):
                #print('found', num)
                card_temp.append('--')
            else:
                card_temp.append(c)
        self.card = card_temp

    def show(self):
        print('игрок:', self.name)
        for j in range(3):
            line = ''
            line2=''
            for c in self.card:
                line = line + '!' + c + '!'
                line2=line2 + '+' + '--' + '+'
            print(line)
            #print('+'-'*len(line)+'+')
            #print(line2)

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
    #print(markers)
num = input('введите число игроков 0- <Enter>=[2]:') or '2'
while int(num) <= 2:
    players = []
    for i in range(int(num)):
        name = input('введите имя игрока' + str(i) + 'или <Enter>=[comp'+ str(i)+']') or 'comp'+str(i)
    print('минимальное количество - 2 игрока!')

    p = Player(5, name)
    players.append((p))
    p.show()
    count = 0
    all = len(markers)
    print(markers)
    for m in markers:
        print('!!!!!!!!!!!!!!!!!!!00000',m,all)
        count = count+1
        print('игровой прогресс1..........'+str(count)+'from:::::::::::'+'всего осталось'+str(all-count))
        print('бочка номер:............'+str(m))
        for p in players:
            print('игрок...........................',p.name)
            print(p.winner)

        p.show()
    print('игровой прогресс2..........' + str(count) + 'from:::::::' + str(all) + str(all - count))

    #num = input('закрыть цифру закрыть:<Enter>=['+str(m)+']') or m

    p.close(int(m))
    print(m, p.name,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    p.show()
    if p.iswinner():
        print('победил игрок!!!!!!!!!!!!!!!!!!!!!!!!!!!!', p.name)

    print('введена некорректная цифра')
    p.show()
    if name == 'comp':
        print(name)

        for m in markers:
            print('бочка номер', m)
            for p in players:
                print('игрок in loop', p.name)
                #num = input('какую цифру закрыть<Enter>=?['+str(m)+']') or m
                if p.name == 'comp':
                    p.close(int(m))
                p.close(int(num))

                p.show()
