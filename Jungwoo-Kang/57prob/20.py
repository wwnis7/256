order_amount = input('What is the order amount? ')
state = input('What state do you live in? ')
county = input('What county do you live in? ')

tax = 0.0
if state == 'Wisconsin':
    if county == 'Eau claire':
        tax = (float(order_amount)) * 0.005
    elif county == 'Dunn':
        tax = float(order_amount) * 0.004
elif state == 'Illinois':
    tax = float(order_amount) * 0.08
else:
    tax = 0

total = float(order_amount) + tax

print(f'The tax is ${tax}.')
print(f'The total is ${total}.')
