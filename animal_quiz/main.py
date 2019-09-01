print("Guess the animal!")
score = 0


def check_guess(guess, answer):
    global score
    if guess == answer:
        print("Correct answer")
        score += 1


guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")

print("Your score is: " + str(score))
