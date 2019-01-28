alcohol=input("amount of consumed alcohol: ")
W=input("weight?")
gender=input('gender?')
H=input('the amount of time since your last drink')

if gender is 'M':
    r=0.73
elif gender is 'W':
    r=0.66
else:
    print('you type improper gender.')

BAC= (float(alcohol)*5.14/float(W)*r) - 0.015*float(H)

print(f"Your BAC is {BAC}")
if BAC>=0.08:
    print('It is not legal for you to drive')
else:
    pass
# BAC = (A × 5.14 / W × r) − .015 × H