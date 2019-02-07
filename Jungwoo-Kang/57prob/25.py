set = []


def passwordValidator():
    a = input('password:')
    for i in a:
        b = ord(i)
        if b >= 48 and b <= 57:
            c = 'number'
            set.append(c)
        elif (b >= 65 and b <= 90) or (b >= 97 and b <= 122):
            c = 'alphabet'
            set.append(c)
        else:
            c = 'special'
            set.append(c)
    if 'number' in set or 'alphabet' in set:
        if 'special' in set and len(a) >= 8:
            print(f'The password {a} is very strong.')
        elif len(a) >= 8 or 'special' in set:
            print(f'The password {a} is strong.')
        else:
            print(f'The password {a} is weak.')
    else:
        if len(a) >= 8:
            print(f'The password {a} is strong.')
        else:
            print(f'The password {a} is weak.')
    print(set)
    print(len(a))

passwordValidator()

#왜 특수문자 하나만 했는데 strong이 뜨는거지.... 첫번쨰 elif에 걸리는데;---17line에서 in set을 앞뒤에 다 붙여야함
# if 'number'는 True로 돌아감
