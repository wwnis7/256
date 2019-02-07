# Enter a number: 100
# Enter a number: 200
# Enter a number: 1000
# Enter a number: 300
# Enter a number: done
# Numbers: 100, 200, 1000, 300
# The average is 400.
# The minimum is 100.
# The maximum is 1000.
# The standard deviation is 400.25.
# import numpy as np
number=''
list=[]
while number != 'done':
    number=input('Enter a number: ')
    list.append(number)
list.remove('done')
print(list)  #list 항목들만 보는법

# avg=np.average(list)
avg=sum(list)/len(list)
min=min(list)
max=max(list)
# sd=np.sd(list)


# print(f'The average is {avg}.')
print(f'The minimum is {min}.')
print(f'The maximum is {max}.')
# print(f'The standard deviation is {sd}.')

