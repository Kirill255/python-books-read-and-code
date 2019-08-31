import random


def hangman(word):
    wrong = 0
    stages = ["",
              "__________      ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            """
            выше мы используем метод index который возвращает первое совпадение,
            поэтому нам нужно заменить правильно совпавший символ, например на знак $
            """
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))  # текущее слово
        e = wrong + 1  # +1 потому что срез не включает правую границу [0: e], а нам нужно включительно
        print("\n".join(stages[0: e]))  # текущая висилица
        if "__" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        # print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))


words = ["кот", "ливень", "лук"]

# ind = random.randint(0, len(words) - 1)
# rword = words[ind]

rword = random.choice(words)  # так проще
# print(rword)

hangman(rword)
