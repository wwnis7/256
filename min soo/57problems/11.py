import math
rate_from = {'Euros': 137.51, '$': 100, 'KRW': 123, 'China': 111}
rate_to = {'Euros': 137.51, '$': 100, 'KRW': 123, 'China': 111}
A = rate_to.keys()
def exchange(x,y,z):
    try:
        x_rate_from, x_rate_to, z = rate_from[x], rate_to[y], float(z)
        ex_rate = float(x_rate_to)/float(x_rate_from)
        amount_to = math.ceil(float(z*x_rate_from) / float(x_rate_to))
        print(f'The exchanging rate is {ex_rate:.2f}.')
        print(f'{z} {x} at an exchanging rate of {ex_rate:.2f} is {amount_to} {y}')
    except: return 0

a = input(f'Which one do you want to exchange from? {list(A)}')
b = input(f'Which one do you want to exchange to? {list(A)}')
c = input(f"How many {a} are you exchanging?")

while exchange(a, b, c) == 0:
    print('Invalid')
    a = input(f'Which one do you want to exchange from? {list(A)}')
    b = input(f'Which one do you want to exchange to? {list(A)}')
    c = input(f"How many {a} are you exchanging?")
