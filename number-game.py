""" 
Number Game
you get 3 chances
every time you guess wrong a new number is generated
"""
import random

chances = 0

while chances < 3:
    try:
        guess = int(input('Enter A Random Number '))
        answer = random.randrange(1, 10)
        if guess == answer:
            print('Correct')
            break
        elif guess != answer:
            print('Wrong')
            chances += 1
        if chances == 3:
            print('Sorry You have guessed wrong please try again')
    except ValueError:
        print('You Must Enter A Number')

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






