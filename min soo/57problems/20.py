W = {'WI', 'WISCONSIN'}
I = {'ILLINOIS', 'IL'}
W1 = {'EAU CLAIRE': 0.5, 'DUNN': 0.4}
while 1:
    amount = input('What is the order amount?')
    try:
        amount = float(amount)
        break
    except: print('invalid')
state = input('What state do you live in?')
if state.upper() in I:
    r = 8
    print('''"The state tax is ${:.2f}"
"The total tax is ${:.2f}"
"The total is ${:.2f}"'''.format(amount*0.01*r, amount*0.01*r, amount*(1+0.01*r)))
elif state.upper() in W:
    r = 5.5
    county = input('What county do you live in?')
    if county.upper() in W1:
        r1 = float(W1[county.upper()])
        r2 = r + r1
        print(f'''"The state tax is ${amount*0.01*r:.2f}"
"The county tax is ${amount*0.01*r1:.2f}"
"The total tax is ${amount*0.01*r2:.2f}"
"The total is ${amount*(1+0.01*r2):.2f}"''')
    if county.upper() not in W1:
        print(f'''"The state tax is ${amount*0.01*r:.2f}"
"The total tax is ${amount*0.01*r:.2f}"
"The total is ${amount*(1+0.01*r):.2f}"''')
else:
    r = 5.5
    print(f'''"The total is ${amount*(1+0.01*r):.2f}"''')


# # challenge 마지막
# W = {'WI', 'WISCONSIN'}
# I = {'ILLINOIS', 'IL'}
# W1 = {'EAU CLAIRE': 0.5, 'DUNN': 0.4}
# while 1:
#     amount = input('What is the order amount?')
#     try:
#         amount = float(amount)
#         break
#     except: print('invalid')
# state = input('What state do you live in?')
# county = input('What county do you live in?')
# if state.upper() in I:
#     r = 8
#     print(f'''"The state tax is ${amount*0.01*r:.2f}"
# "The total tax is ${amount*0.01*r:.2f}"
# "The total is ${amount*(1+0.01*r):.2f}"''')
# elif state.upper() in W and county.upper() in W1:
#     r = 5.5
#     r1 = float(W1[county.upper()])
#     r2 = r + r1
#     print(f'''"The state tax is ${amount*0.01*r:.2f}"
# "The county tax is ${amount*0.01*r1:.2f}"
# "The total tax is ${amount*0.01*r2:.2f}"
# "The total is ${amount*(1+0.01*r2):.2f}"''')
# elif state.upper() in W and county.upper() not in W1:
#     r = 5.5
#     print(f'''"The state tax is ${amount*0.01*r:.2f}"
# "The total tax is ${amount*0.01  :.2f}"
# "The total is ${amount*(1+0.01*r):.2f}"''')
# else:
#     r = 5.5
#     print(f'''"The total is ${amount*(1+0.01*r):.2f}"''')