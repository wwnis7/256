D = {'FT':12, 'FEET': 12, 'CM': 0.39, 'IN':1, 'INCH':1, 'IN.':1, 'KG':2.2, 'KILOGRAM':2.2, 'LB':1, 'POUND':1, 'LBS':1}

while 1:
    w_unit = input('Select unit of weight: kg, lb ')
    if w_unit.upper() not in D: print('Invalid')
    else: break
while 1:
    w = input('Enter your weight')
    try:
        w_float = float(w)
        break
    except: print('Invalid')
while 1:
    h_unit = input('Select unit of height: ft, cm, in. ')
    if h_unit.upper() not in D: print('Invalid')
    else: break
while 1:
    h = input('Enter your height')
    try:
        h_float = float(h)
        break
    except: print('Invalid')

w1 = w_float*float(D[w_unit.upper()])
h1 = h_float*D[h_unit.upper()]

BMI = (w1/h1**2)*703
print('Your BMI is {:.1f}.'.format(BMI))

if 18.5 <= BMI <= 25:
    print('You are within the ideal weight range')
elif BMI < 18.5:
    print('You are underweight. You should see your doctor.')
elif BMI > 25:
    print('You are overweight. You should see your doctor.')
else:
    print('Your BMI cannot be calculated.')



# import re
# D = {'FT':12, 'FEET': 12, 'CM': 0.39, 'IN':1, 'INCH':1, 'IN.':1, 'KG':2.2, 'KILOGRAM':2.2, 'LB':1, 'POUND':1, 'LBS':1}
# w_input = input('Write your weight: ex) 70kg')
# h_input = input('Write your height: ex) 177cm')
#
# w_float = float(re.findall('[^a-zA-Z]+', w_input)[0])
# w_unit = re.findall('[a-zA-Z]+',w_input)[0]
#
# h_float = float(re.findall('[^a-zA-Z]+',h_input)[0])
# h_unit = re.findall('[a-zA-Z]+',h_input)[0]
#
# w = w_float*float(D[w_unit.upper()])
# h = h_float*D[h_unit.upper()]
#
# BMI = (w/h**2)*703
# print('Your BMI is {:.1f}.'.format(BMI))
#
# if 18.5 <= BMI <= 25:
#     print('You are within the ideal weight range')
# elif BMI < 18.5:
#     print('You are underweight. You should see your doctor.')
# elif BMI > 25:
#     print('You are overweight. You should see your doctor.')
# else:
#     print('Your BMI cannot be calculated.')