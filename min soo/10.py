D = {'item 1':25, 'item 2':10, 'item 3':4, 'item 4':2}
p = []
Subtotal = 0
tax_rate = 5.5                                                          # 5.5%
while 1:
    item = input(f'''
Enter the item you will purchase {list(D.keys())},
or Press "Done" if you want to finish.: ''')
    if item.upper() == 'DONE':
        break
    else:
        while 1:
            try:
                price = f'Price of {item.lower()}: {D[item.lower()]}'
                print(price)
                break
            except:
                item = input(f'''
The item does not exist.
Enter the item you will purchase {list(D.keys())},
or Press "Done" if you want to finish.: ''')
    while 1:
        quantity = input(f'Quantity of {item.lower()}: ')
        quantity1 = f'Quantity of {item.lower()}: {quantity}'
        if quantity.isdigit():
            quantity = int(quantity)
            break
        else:
            try:
                quantity = float(quantity)
                break
            except: print('You should enter the quantity by numeric type.')
    Subtotal += D[item.lower()] * quantity
    p.append(price)
    p.append(quantity1)

Tax = Subtotal*0.01*tax_rate
Total = Subtotal + Tax
print()
for x in p:
    print(x)
print(f'''Subtotal: ${Subtotal}
Tax: ${Tax}
Total: ${Total}''')