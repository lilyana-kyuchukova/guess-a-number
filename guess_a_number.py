import random

computer_number = random.randint(1, 100)
not_guessed = True

while not_guessed:

    player_number = int(input("Pick a number between 1 and 100: "))

    if player_number == computer_number:
        print()

