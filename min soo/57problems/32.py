from random import randint as rd
c = 'y'
while c == 'y':
    i = 0
    while 1:
        a = input('Pick a difficulty level (1, 2, 3, or else): ')
        try:
            a = int(a)
            break
        except: print('Invalid.')
    x = rd(1, 10**a)
    print(f'Answer is {x}.')
    b = input("I have my number. What's your guess?")
    while b != x:
        i += 1
        try:
            b = int(b)
            if b < x:
                b = input('Too low. Guess again: ')
            elif b > x:
                b = input('Too high. Guess again.')
            else: pass
        except: b = input('Invalid Type. Enter the number you guess.')              # i -= 1 : 잘못 입력 카운트 안 하기
    if i == 1: print(f'You\'re a mind reader! You got it in {i} guesses!')
    elif 2<= i <5: print(f'Most impressive. You got it in {i} guesses!')
    elif 5<= i <7: print(f'You can do better than that. You got it in {i} guesses!')
    else: print(f'Better luck next time. You got it in {i} guesses!')
    while c != 'n':
        c = input('Play again? y/n ')
        if c.upper() in ['Y', 'N']:
            D = {'Y': "Let's play again!", 'N': 'Goodbye!'}
            print(f'{D[c.upper()]}')
            break
        else: print('Invalid.')