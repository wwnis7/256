import math
def calculateMonthsUntilPaidOff(b,i,p):
    try:
        b, i, p = float(b), float(i), round(float(p),2)
        n = math.ceil((-1/30)*(math.log(1+(b/p)*(1-(1+0.01*i/365)**30)))/(math.log(1+0.01*i/365)))
        return n
    except: print('Invalid')

def calculateAmountPaidPerMonth(b,i,n):
    try:
        b, i, n = float(b), float(i), math.ceil(float(n))
        p = b*(1-(1+0.01*i/365)**30)/((1+0.01*i/365)**(-30*n)-1)
        return p
    except: print('Invalid')

while 1:
    c = input('Choose the value you want. The number of month(Press "n") or the monthly payment(Press "p")? ')
    if c.lower() == 'n':
        print(f"It will take you {calculateMonthsUntilPaidOff(input('What is your balance? '), input('What is the APR on the card (as a percent)? '), input('What is the monthly payment you can make? '))} months to pay off this card.")
        break
    elif c.lower() == 'p':
        print(f"It will need {calculateAmountPaidPerMonth(input('What is your balance? '), input('What is the APR on the card (as a percent)? '), input('What is the number of month? ')):.2f} payments to pay per month. ")
        break
    else: print('Invalid')