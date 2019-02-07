# Enter a list of numbers, separated by spaces: 1 2 3 4 5 6 7 8
# The even numbers are 2 4 6 8.


list = input('Enter a list of numbers, separated by spaces: ').split(' ')
even = []
for i in list:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        continue
result=' '.join(even)
print(f'The even numbers are {result}.')

#join함수 사용!