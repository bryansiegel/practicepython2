"""
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
"""

try:
    number = int(input('Please Enter A Number '))
    if number % 2 == 0:
        print('The Number Is Even')
    elif number % 4 == 0:
        print('The Number can be divided by 4')
    else:
        print('The Number is Odd')
except ValueError:
    print('You Must Enter A Number')
