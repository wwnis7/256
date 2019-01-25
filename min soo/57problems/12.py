while 1:
    P = input('Enter the principal')
    r = input('Enter the rate of interest( %)')
    t = input('Enter the number of years')
    try:
        P, r, t = float(P), float(r), float(t)
        break
    except: print('Please enter the numeric values.')
A = lambda P, r, t: print(f'After {t} years at {r}%, the investment will be worth ${float(P)*(1+0.01*float(r)*float(t)):.2f}')
A(P,r,t)
for i in range(1,int(t+1)):
    A(P, r, i)
