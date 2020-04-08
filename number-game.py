""" 
Number Game
you get 3 chances
every time you guess wrong a new number is generated
"""
import random

chances = 0

# Max 3 chances
while chances < 3:
    # TODO: check input to make sure it's an int
    guess = input('Enter A Random Number ')
    answer = random.randrange(1,10)
    # answer = 3

# convert input guess variable into int
    if int(guess) == answer:
        print('Correct')
        break
    elif int(guess) != answer:
        print('Wrong')
        # print(type(guess))
        # print(type(answer))
        chances += 1
# break out of the while loop once you hit 3 chances
if chances == 3:
    print('Sorry You have guessed wrong please try again')
"""
Old Code
"""
# try:
#     b = input('Enter A Random Number ')
#     f = random.randrange(1, 3)

#     if int(b) != f:
#         print('Wrong')
#         b = input('Enter A Random Number Again')
#     elif int(b) == f:
#         print('Correct')
# except ValueError:
#     print('You Must Enter A Number. Please Try Again')
#     b = input('Lets Try Again')
#     if int(b) != f:
#         print('Wrong Again')
#     elif int(b) == f:
#         print('Correct')
"""
Old Code End
"""






