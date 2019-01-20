while 1:
    people = input('How many people? ')
    pizzas = input('How many pizzas do you have? ')
    pieces = input('''
How many pieces are in a pizza? ''')
    try:
        people, pizzas, pieces = int(people), int(pizzas), int(pieces)              # int()는 str과 float을 받을 때 각각 다르게 행동한다. str은 받으면 isdigit(정수) type만 받을 수 있고, float은 임의의 수를 받되 정수부분을 버린 값을 출력한다.
        break
    except: print('Invalid.')
each = pizzas*pieces // people
leftover = pizzas*pieces % each
if each in [0,1]: num = ''
else: num = 's'
if leftover in [0,1]: num1 = ''
else: num1 = 's'
print(f'''Each person gets {each} piece{num} of pizza.
There are {leftover} leftover piece{num1}.''')

# while 1:
#     people = input('How many people? ')
#     pizzas = input('How many pizzas do you have? ')
#     pieces = input('''
# How many pieces are in a pizza? ''')
#     if people.isdigit() and pizzas.isdigit() and pieces.isdigit():
#         people, pizzas, pieces = int(people), int(pizzas), int(pieces)
#         break
#     else: print('Invalid.')
# each = pizzas*pieces // people
# leftover = pizzas*pieces % each
# print(f'''Each person gets {each} pieces of pizza.
# There are {leftover} leftover pieces.'''

# #Chalenge
# while 1:
#     people = input('How many people?')
#     each = input('How many pieces of pizza each person gets?')
#     pieces = input('''
# How many pieces are in a pizza? ''')
#     try:
#         people, each, pieces = int(people), int(each), int(pieces)
#         break
#     except: print('Invalid')
# pizzas = people * each // pieces
# if people * each % pieces > 0:
#     pizzas += 1
# leftover = pizzas*pieces - each*people
# if pizzas in [0,1]: num0 = ' is'
# else: num0 = 's are'
# if each in [0,1]: num = ''
# else: num = 's'
# if leftover in [0,1]: num1, verbe = '', 'is'
# else: num1, verbe = 's', 'are'
# print(f'''{pizzas} pizza{num0} required.
# Each person gets {each} piece{num} of pizza.
# There {verbe} {leftover} leftover piece{num1}.''')