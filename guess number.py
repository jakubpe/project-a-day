import random


def player_guess(guess):
    if guess == number_guess:
        print("The number is {}. You win".format(guess))
        return 0
    elif guess > number_guess:
        print("Too high. Guess again.")
        return 1
    else:
        print("Too low. Guess again.")
        return 1


def mode(level):
    if level == 'easy':
        return 10
    else:
        return 5


next_round = True
while next_round:
    number_guess = random.randint(1, 100)
    continue_game = True
    lives = mode(input("For easy level 'easy', for hard level 'hard': "))
    while continue_game:
        if lives > 0:
            continue_game = player_guess(int(input("Guess a number: ")))
            lives -= 1
            if continue_game:
                print("You have {} lives left.".format(lives))
        else:
            print("No more lives. You lost.")
            continue_game = False
    if input("Do you want to play again? y/n ") == 'n':
        next_round = False
