
people=input('How many people? ')
pizzas=input('How many pizzas do you have? ')
num_pizzas=8*int(pizzas)
get=num_pizzas/int(people)
leftover=num_pizzas%int(people)
print('''%d people with %d pizzas
        Each person gets %d pieces of pizza.
        There are %d leftover pieces.'''%(int(people),int(pizzas),get,leftover))
