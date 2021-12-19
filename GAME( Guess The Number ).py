'''
    GAME:
        Guess The Number
        
'''

import random

print('Choose a Number Between 0 & 10')
n=random.randrange(0,10)

f='no'

while f == 'no':
    a=int(input('Your Choice Is: '))

    if a < n:
        print('You Lose , Increase Your Amount')

    elif a > n:
        print('Decrease Your Amount')
    
    else:
        print('Correct , You Win ')

    

