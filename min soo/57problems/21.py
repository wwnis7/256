D1 = {1:'January', 2:'February', 3:'March', 4:'april', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
D2 = {1:'1월', 2:'2월', 3:'3월', 4:'4월', 5:'5월', 6:'6월', 7:'7월', 8:'8월', 9:'9월', 10:'10월', 11:'11월', 12:'12월'}

while 1:
    S = input('Select the language: kor or eng ')
    if S.lower() == 'eng':
        D = D1
    elif S.lower() == 'kor':
        D = D2
    else:
        print('Invalid')
        continue
    try:
        Month = D[int(input('Please enter the number of the month: '))]
        break
    except: print('Invalid')

print(f'The name of the month is {Month}.')