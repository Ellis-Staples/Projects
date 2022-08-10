from random import random


import random

top_of_range = input ('type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print ('please enter a number greater than zero')
        quit()
else:
    print ('please enter a number next time')
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input (' make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print ('please enter a number next time')
        continue

    if user_guess == random_number:
        print ('Correct answer')
        break
    elif user_guess > random_number:
            print ('you were greater than the number')
    else:
            print (' you were less than the number')


print ('you got it in', guesses, 'guesses')




