import math
while 1:
    P = input('What is the principal amount?')
    r = input('What is the rate? ( %)')
    t = input('What is the number of years?')
    n = input('What is the number of times the interest is compounded per year: ')
    try:
        P, r, t, n = float(P), float(r), float(t), float(n)
        break
    except: print('Invalid')
A = P*(1+r/(100*n))**(n*t)
print(f'${P} invested at {r}% for {t} years compounded {n} times per year is ${math.ceil(A*100)/100}')

# challenge
# while 1:
#     A = input('What is the compound?')
#     r = input('What is the rate? ( %)')
#     t = input('What is the number of years?')
#     n = input('What is the number of times the interest is compounded per year: ')
#     try:
#         A, r, t, n = float(A), float(r), float(t), float(n)
#         break
#     except: print('Invalid')
# P = A / (1+r/(100*n))**(n*t)
# print(f'${math.ceil(P*100)/100} is required at {r}% for {t} years compounded {n} times per year to arrive the compound {A}')