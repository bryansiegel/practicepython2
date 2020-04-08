"""
http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
name = input('Please Enter Your Name ')
age = int(input('Please Enter Your Age '))
when_one_hundred = 100 - age
# TODO: make sure years is not greater than 100 or less than 0
print(f'Hi {name} you are {age} years old')
print(f'You will 100 in {when_one_hundred} years. ')