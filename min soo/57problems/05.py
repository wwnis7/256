while 1:
    try:
        a = float(input('What is the first number? '))
        b = float(input('What is the second number?'))
        break
    except: print('Invalid. Enter the numeric types.')
cal = lambda x,y: print(f'''{x} + {y} = {x+y}
{x} - {y} = {x-y}
{x} x {y} = {x*y}
{x} / {y} = {x/y}''')
cal(a,b)
