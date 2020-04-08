"""
99 Bottles of Beer on the wall
"""
# bottles_of_beer = 99

# while bottles_of_beer <= 99:
#     print(f'I have {bottles_of_beer} Bottles of Beer. Take One Down and Pass it around' )
#     bottles_of_beer += 1
#     print(f'{bottles_of_beer} Bottles of Beer on the Wall')

for bottles_of_beer in range(99,-0,-1):
    if bottles_of_beer == 1:
        print(f'I have {bottles_of_beer} Bottle of Beer. Take One Down and Pass it Around ')
        print(f'{bottles_of_beer} Bottle of Beer on the Wall')
    else:
        print(f'I have {bottles_of_beer} Bottles of Beer. Take One Down and Pass it Around ')
        print(f'{bottles_of_beer} Bottles of Beer on the Wall')
        
        # print(f'{bottles_of_beer} On the Wall')
    # elif bottles_of_beer == 1:
    #     print(f'I have {bottles_of_beer} Bottle of Beer. Take One Down and Pass it Around')
    #     break
