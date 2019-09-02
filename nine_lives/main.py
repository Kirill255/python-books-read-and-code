from random import choice

# для удобства у нас все слова из 5 букв
words = ["pizza", "fairy", "teeth",
         "shirt", "otter", "plane",
         "brush", "horse", "light"
         ]
secret_word = choice(words)
board = list("?????")  # 5шт по кол-ву букв в словах ['?', '?', '?', '?', '?']
lives = 12
heart_symbol = u"\u2764"  # ❤
guessed_word_correctly = False


# обновляем слово на доске, функция вызывается только если введённая пользователем буква, точно присутствует в слове
# цикл нужен что бы открыть все совпадающие буквы, например в слове pizza две буквы z
def update_clue(guessed_letter, secret_word, board):
    index = 0
    # перебираем слово и сравнимаем каждую букву с буквой пользователя, когда находим совпадение, то выводим на доске
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            board[index] = guessed_letter
        index += 1


# запуск программы
difficulty = int(input("Choose difficulty (type 1, 2, 3):\n 1 Easy\n 2 Normal\n 3 Hard\n"))
# если пользователь введёт другое число, тогда число жизней останется равно 12
if 3 >= difficulty >= 1:
    lives /= difficulty  # 12/1 = 12.0, 12/2 = 6.0, 12/3 = 4.0
    lives = int(lives)  # потому что после деления получается float число

while lives > 0:
    print(board)  # распечатываем доску
    print("Lives left: " + heart_symbol * lives)  # кол-во жизней
    guess = input("Guess a letter or the whole word: ")  # спрашиваем букву или слово целиком

    # сравниваем слово целиком
    if guess == secret_word:
        guessed_word_correctly = True
        break

    # сравниваем побуквенно, если буквы точно есть в слове, обновляем доску
    if guess in secret_word:
        update_clue(guess, secret_word, board)

        # проверяем отгадано ли слово целиком
        if "".join(board) == secret_word:
            guessed_word_correctly = True
            break
    else:
        # инчае буква неверная, вычитаем жизнь
        print("Incorrect. You lose a life")
        lives -= 1

if guessed_word_correctly:
    print("You won! The secret word was " + secret_word)
else:
    print("You lost! The secret word was " + secret_word)
