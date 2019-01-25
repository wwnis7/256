A = {'WI', 'NY', 'LA','WISCONSIN', 'NEW YORK', 'LOS ANGELES'}
while 1:
    amount = input('What is the order amount?')
    try:
        amount = float(amount)
        break
    except: print('Invalid')
state = input('What is the state?')
r = 5.5
subtotal = amount
tax = 0.01 * r * amount
total = amount * (1 + 0.01 * r)
if state.upper() in A:
    print(f"""The subtotal is ${subtotal:.2f}
The tax is ${tax:.2f}
The total is {total:.2f}""")
if state.upper not in A:
    print(f'The total is ${total:.2f}')