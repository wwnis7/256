first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
third_num = input("Enter the third number: ")

if float(first_num) == float(second_num) or float(first_num) == float(third_num) or float(third_num) == float(
        second_num):
    print('There is the same number')
else:
    largest_num = max(float(first_num), float(second_num), float(third_num))
    print(f'The largest number is {largest_num}.')
