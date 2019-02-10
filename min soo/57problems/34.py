A = ['John Smith', 'Jackie jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
for j in range(2):
    print(f'There are {len(A)} employees: ')
    for i in A:
        print(i)
    if j == 1: break
    name = input('Enter an employee name to remove: ')
    try:
        A.remove(name)
    except:
        print(f'{name} is not an employee.')