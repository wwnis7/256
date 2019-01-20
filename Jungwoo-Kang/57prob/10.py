

item1_p=input('Enter the price of item 1 ')
item1_q=input('Enter the quantity of item 1 ')
item2_p=input('Enter the price of item 2 ')
item2_q=input('Enter the quantity of item 2 ')
item3_p=input('Enter the price of item 3 ')
item3_q=input('Enter the quantity of item 3 ')
subtotal=int(item1_p)*int(item1_q)+int(item2_p)*int(item2_q)+int(item3_p)*int(item3_q)
tax=float(subtotal)*0.055
total=subtotal+tax
#print(type(subtotal))
#print(tax)
#print(total)

print('Subtotal:$%d'% subtotal)
print('Tax:$%f'% round(tax,2))
print('Total:$%f'% round(total,2))