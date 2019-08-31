from random import shuffle


class Card:
    # первые два значения None сделаны для удобства, что бы индекс совпадал со значением, values[5] == "5"
    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "валет", "дама",
              "король", "туз"
              ]

    suits = ["пикей",
             "червей",
             "бубей",
             "треф"
             ]

    # value и suit целые числа, мы будем генерироать карты в цикле, Card(4, 1) -> четвёрка червей
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # переопределяем методы сравнения для карт
    def __lt__(self, c2):
        if self.value < c2.value:  # сначала по значению сравниваем
            return True
        if self.value == c2.value:  # если значения равны
            if self.suit < c2.suit:  # то по масти, масти упорядочены в списке по возрастанию силы, самая сильная "треф"
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False

    # переопределяем метод, теперь он выодит название карты
    def __repr__(self):
        v = self.values[self.value] + " " + self.suits[self.suit]
        return v


class Deck:
    # генерируем 52-карточную колоду и сразу перемешиваем
    def __init__(self):
        self.cards = []
        for i in range(2, 15):  # первое значение 2(двойка), последнее 14(туз)
            for j in range(4):  # масти от 0 до 3, см. список мастей
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.card = None  # текущая карта игрока
        self.wins = 0  # кол-во выигранных раундов


class Game:
    def __init__(self):
        name1 = input("Имя первого игрока: ")
        name2 = input("Имя второго игрока: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} забирает карты"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} кладёт {}, а {} кладёт {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            m = "Нажмите X для выхода. Нажмите любую другую клавишу для начала игры"
            r = input(m)
            if r == "X":
                break

            p1n = self.p1.name
            p2n = self.p2.name

            # вынимаем карты из колоды и назначаем игрокам
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()

            self.draw(p1n, p1c, p2n, p2c)  # отрисовываем ход

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("Игра окончена. {} выиграл!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья!"


game = Game()
game.play_game()
