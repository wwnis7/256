# • n is the number of months.
# • i is the daily rate (APR divided by 365).
# • b is the balance.
# • p is the monthly payment.


import numpy as np
def CMP():
    APR=input("What is the APR on the card (as a percent)?")
    balance=input('What is your balance?')
    payment=input('What is the monthly payment you can make?')
    a=float(APR)
    b=float(balance)
    p=float(payment)
    i=a/365
    n=(-1/30)*(mt.log(1+(b/p)(1-pow(1+i,30))))/mt.log(1+i)
    print(f'It will take you {n} months to pay off this card.')
CMP()

#numpy어딧냐;; float object is no callable?