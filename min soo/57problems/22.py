# A = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
A = ['1st']
S = []
M = 0
k = 1
while k:
    n = input(f'Enter the {A[-1]} number or "finish": ')
    if n.lower() == 'finish':
        k = 0
        break
    else:
        try:
            j = int(n)
            if j in S:
                k = 0
            else:
                S.append(j)
                if j < M:
                    pass
                else:
                    M = j
            if len(A) % 10 == 0:
                s = f'{len(A) + 1}st'
            elif len(A) % 10 == 1:
                s = f'{len(A) + 1}nd'
            elif len(A) % 10 == 2:
                s = f'{len(A) + 1}rd'
            else:
                s = f'{len(A) + 1}th'
            A.append(s)
        except:
            print('Invalid.')

if len(A) == 1:
    print('You did not enter any number')
elif n.lower() == 'finish':
    print(f'The largest number is {M}.')
else:
    print('You enter a repeated number. Shut down')