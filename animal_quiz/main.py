print("Guess the animal!")
score = 0


def check_guess(guess, answer):
    global score  # global значит что мы используем глобальную переменную, объявленную выше
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer.")
            # с каждым неправильным ответом кол-во очков которые можно получить за ответ, уменьшается
            score = score + 3 - attempt  # максимум 3
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer. Try again: ")
            attempt += 1

    if attempt == 3:
        print("The correct answer is: " + answer)


guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")

guess4 = input("Which one of these is a fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
Type A, B, C, or D: ")
check_guess(guess4, "C")

guess5 = input("Mice are mammals. True or False? ")
check_guess(guess5, "True")

print("Your score is: " + str(score))
