while 1:
    age = input('What is your age?')
    try:
        age = int(age)
        break
    except: print('Invalid')
if age >= 19:
    a = ''
else:
    a = 'not '
print(f'You are {a}old enough to legally drive.')