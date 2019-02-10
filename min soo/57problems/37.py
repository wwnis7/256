import random
import string
while 1:
    a = input("What's the minimum length? ")
    b = input('How many special characters? ')
    c = input('How many numbers? ')
    try:
        a, b, c = int(a), int(b), int(c)
        if a > 0 and b >= 0 and c >= 0:
            break
        else: print('Invalid')
    except: print('Invalid')
M = max(a, b + c)
alph_min = M - b - c
L = 0
while L < alph_min:
    i = 0
    while i != 1:                                          # uniform distribution을 이용하여 length를 정해준다. 더 정확히는 geometric distribution을 이용한 것임.
        i = random.randint(0,alph_min + 1)
        L += 1                                             # L은 alph_length 이다
while 1:
    n = input("The number of passwords which you'll create")
    try:
        n = int(n)
        break
    except: print('Invalid')
A = []
B = []
for j in range(n):
    pw = ''
    for i in range(L):
        pw = pw + random.choice(string.ascii_lowercase)
    for i in range(b):
        pw = pw + random.choice(string.punctuation)
    for i in range(c):
        pw = pw + str(random.randint(0,9))
    password = ''.join(random.sample(pw,len(pw)))
    print(f'''{j+1}'s password of is:
{password}''')
    D = ['a','e','i','o','u']
    password_1 = ''
    for i in password:
        if i in D:
            password_1 = password_1 + str(random.randint(0,9))
        else: password_1 = password_1 + i
    print(f'''Collections -> numbers. {j+1}'s changed password is:
{password_1}''')
    print()
    A.append(password)
    B.append(password_1)
print('Your password set is: ', A)
print('Your changed password set is: ', B)