from random import randint
minimum = 1
maximum = 100
my_number = randint(minimum, maximum)
game_set = False
while not game_set: 
    guess = input(f'Guess my number from {minimum} to {maximum}: ')
    # print(f'Your guess is {guess}')
    guess = int(guess)
    game_set = False
    print(f'Your guess is {guess}')
    if my_number == guess :
        print('You won! That is my number!')
        game_set = True
    elif guess > my_number:
        print('My number is lower than your guess!')
        maximum = guess
    elif guess < my_number:
        print('My number is larger than your guess!')
        minimum = guess