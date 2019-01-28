# 종합문제1
num = input('Enter the number')
if len(num)>0: result = num[0]
else: result = ''
for i in range(1,len(num)):
    try:
        a, b = int(num[i-1]), int(num[i])
        if (a**2 + b**2) % 4 == 2: result = result + '-' + num[i]
        elif (a**2 + b**2) % 4 == 0: result = result + '*' + num[i]
        else: result += num[i]
    except: result += num[i]
print(result)

# 종합문제2
str = input('Enter the string')
I = ''
while len(str) > 0:
    i = 0
    while str[0] == str[i]:
        i += 1
        if i == len(str): break
    I = I + str[0] + f'{i}'
    str = str[i:]
print(I)

# 종합문제3
num = input('Enter the number')
b = num.split()
result = list()
for x in b:
    if '0123456789' == ''.join(sorted(x)): result.append('true')
    else: result.append('false')
print(' '.join(result))

# num = input('Enter the number')
# b = num.split()
# result = ''
# for x in b:
#     if '0123456789' == ''.join(sorted(x)): result += 'true '
#     else: result += 'false '
# print(result)

# num = input('Enter the number')
# b = num.split()
# result = list()
# for x in b:
#     result.append('0123456789' == ''.join(sorted(x)))
# print(result)
# # 0123456789 01234 01234567890 6789012345 012322456789

# 종합문제4
#.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
D = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M',
     '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z',
     '':' '}
msg = input('Enter the mos code')
M = msg.split(' ')
I = list()
for x in M:
    try: I.append(D[x])
    except: pass
print(''.join(I))