b = 1
while b:
    story = lambda noun, verb, adjective, adverb: print(f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!')
    story(input('Enter a noun: '), input('Enter a verb: '), input('Enter an adjective: '), input('Enter an adverb: '))
    while 1:
        a = input('Do you want to continue the game? y/n')
        if a.upper() == 'y'.upper():
            break
        elif a.upper() == 'n'.upper():
            b = 0
            print('The Game is finished')
            break
        else:
            print('Invalid')