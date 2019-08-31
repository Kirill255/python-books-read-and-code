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


card = Card(2, 1)
card2 = Card(2, 3)

print(card)
print(card2)
print(card < card2)
