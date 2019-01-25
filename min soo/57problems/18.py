while 1:
    a = input('''Press C convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Press CK to convert from Celsius to Kelvin
Press FK to convert from Fahrenheit to Kelvin
Press KC to convert from Kelvin to Celsius
Press KF to convert from Kelvin to Fahrenheit''')
    if a.upper() not in ['C', 'F', 'CK', 'FK', 'KC', 'KF']:
        print('Invalid')
    else: break

def f(x):
    return (x-32)*5/9, (x*9/5)+32   #[C=f(F), F=f(C)]
def g(x): return x - 273, x + 273

print(f'Your choice: {a.upper()}')
if a.upper() == 'C':
    while 1:
        F = input('Please enter the temperature in Fahrenheit: ')
        try:
            F = float(F)
            break
        except: print('Invalid')
    C = f(F)[0]
    print(f'The temperature in Celsius is {C:.2f}.')
elif a.upper() == 'F':
    while 1:
        C = input('Please enter the temperature in Celsius: ')
        try:
            C = float(C)
            break
        except: print('Invalid')
    F = f(C)[1]
    print(f'The temperature in Fahrenheit: {F:.2f}')
elif a.upper() == 'CK':
    while 1:
        C = input('Please enter the temperature in Celsius: ')
        try:
            C = float(C)
            break
        except:
            print('Invalid')
    K = g(C)[0]
    print(f'The temperature in Kelvin is {K:.2f}.')
elif a.upper() == 'FK':
    while 1:
        F = input('Please enter the temperature in Fahrenheit: ')
        try:
            F = float(F)
            break
        except: print('Invalid')
    C = f(F)[0]
    K = g(C)[0]
    print(f'The temperature in Kelvin is {K:.2f}.')
elif a.upper() == 'KC':
    while 1:
        K = input('Please enter the temperature in Kelvin: ')
        try:
            K = float(K)
            break
        except: print('Invalid')
    C = g(K)[1]
    print(f'The temperature in Celsius is {C:.2f}.')
else:                                                                       #'KF'
    while 1:
        K = input('Please enter the temperature in Kelvin: ')
        try:
            K = float(K)
            break
        except: print('Invalid')
    C = g(K)[1]
    F = f(C)[1]
    print(f'The temperature in Fahrenheit: {F:.2f}')