"""
    This program simulates a game where the user tries to guess
    a secret number (integer) chosen at random from a user-defined range. 
    The user wins if the correct number can be guessed before a limited
    number of tries.
"""

import random 

start = int(input('enter a number for the start of the range: '))
stop = int(input('enter a number for the end of the range: '))
interval = 2
secret_number = random.randrange(start, stop, interval)
number_of_tries = 5
count = 0
while count < number_of_tries:
    user_input = input('guess the number: ')
    current_number = int(user_input)
    if current_number == secret_number:
        print('CORRECT!! You win')
        break
    elif current_number < secret_number:
        print('Your guess is too low! Try again!')
    else:
        print('Your guess is too big! Try again!')
    count += 1

if count == number_of_tries:
    print('Better luck next time!')
else:
    print('You\'re great at this! Keep it up')