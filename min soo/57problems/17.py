B = {'NY':0.08, 'LA': 0.09, 'WI': 0.07}
while 1:
    res = input('Write your residence')
    if res in B:
        res = B[res]
        while 1:
            sex = input('Write your sex. Man of Woman?')
            if sex.upper() == 'MAN':
                r = 0.6
                break
            elif sex.upper() == 'WOMAN':
                r = 0.73
                break
            else:
                print('Please state your sex correctly')
        while 1:
            A = input('Write your alcohol consumption')
            W = input('Write your weight')
            H = input('Write the elapsed time after drinking')
            try:
                A, W, H = float(A), float(W), float(H)
                BAC = (A * 5.14 / (W * r)) - 0.15 * H
                break
            except: print('Invalid')
        if BAC >=res:
            print('''Your BAC is {}
It is not legal for you to drive.'''.format(BAC))
        elif BAC < res:
            print('''Your BAC is {}
It is legal for you to drive.'''.format(BAC))
        break
    else:
        print('Please state your residence correctly')