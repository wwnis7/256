# What is the order amount? 10
# What is the state? WI
# The subtotal is $10.00.
# The tax is $0.55.
# The total is $10.55.
# Or
# What is the order amount? 10
# What is the state? MN
# The total is $10.00

amount=input("What is the order amount? ")
state=input("What is the state? ")
if state == "WI":
    tax=float(amount)*0.055
else:
    tax=0
total=float(amount)+tax
print(f'''The subtotal is ${amount}
        The tax is ${tax}
        The total is ${total}''')

#정의를 먼저해야되나?--""써야한다 스트링이라서