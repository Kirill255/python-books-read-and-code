import random
import string

print("Welcome to Password Picker!")

adjectives = ["sleepy", "slow", "smelly",
              "wet", "fat", "red",
              "orange", "yellow", "green",
              "blue", "purple", "fluffy",
              "white", "proud", "brave"
              ]

nouns = ["apple", "dinosaur", "ball",
         "toaster", "goat", "dragon",
         "hammer", "duck", "panda",
         "telephone", "banana", "teacher"
         ]

while True:
    for num in range(3):  # теперь генерируем сразу по 3 пароля
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        sign = random.choice(string.punctuation)  # рандомный знак из строки !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        # print(string.punctuation)

        password = adjective + noun + str(number) + sign
        print("Your new password is: %s" % password)  # fatpanda56= or fluffyduck16+

    response = input("Would you like another password? Type y or n: ")
    if response == "n":
        break
