D = {1:'a very weak', 2:'a weak', 3:'a strong', 4:'a very strong', None:'untyped'}
x = input('Enter your password ')
def passwordValidator():
    if len(x) < 8 and x.isnumeric():
        return 1
    elif len(x) < 8 and x.isalpha():
        return 2
    elif len(x) >= 8 and x.isalnum() and not x.isalpha() and not x.isnumeric():
        return 3
    elif len(x) >= 8 and not x.isalnum():
        for i in x:
            if i.isnumeric():
                for j in x:
                    if j.isalpha():
                        return 4
                    break
                break
# passwordValidator()
print(f"The password '{x}' is {D[passwordValidator()]} password.")