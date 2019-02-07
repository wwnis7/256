while 1:
    rate=input('What is the rate of return? ')
    try:
        r=int(rate)
        y=72/r
        print(f'It will take {y} years to double your initial investment.')
        break
    except:
        print('''Sorry. That's not a valid input.''')
        continue
