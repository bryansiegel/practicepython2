# Practice Python http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import random



# b = int(input(('Enter A Random Number ')))
# f = random.randrange(0,3)


# print(type(b))

def is_int():
    try:
        b = int(input('Enter A Random Number '))
        f = random.randrange(0, 3)
        if b == f:
            print(f'Correct', f)
        elif b != f:
            print(f'Please Try Again',f)
            b = int(input('Enter A Random Number Again '))
        elif b == f:
            print('You Are Right')
        elif b != f:
            print('Your Done')
    except ValueError:
        print('Not An Int Please Try Again')
        b = int(input())

is_int()

# if (b):
#     print('Not int')
#     b = input()
# elif int(b) == f:
#     print(f'Correct', f)
# elif int(b) != f:
#     print('Incorrect')
#     b = input()

# if(type(b) != type(int)):
#     print('Not Int')
#     b = input()
# if int(b) == f:
#     print(f'Correct', f)
# elif int(b) != f:
#     print(f'2nd try Incorrect', f)
#     b = input()





