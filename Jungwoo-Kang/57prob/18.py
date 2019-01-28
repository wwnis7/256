# Press C to convert from Fahrenheit to Celsius.
# Press F to convert from Celsius to Fahrenheit.
# Your choice: C
# Please enter the temperature in Fahrenheit: 32
# The temperature in Celsius is 0.

print('''Press C to convert from Fahrenheit to Celsius.
 Press F to convert from Celsius to Fahrenheit.''')
choice=input()
if choice=='F':
    tem='Fahrenheit'

elif choice=='C':
    tem='Celcius'

else:
    print('you press wrong button')

temperature=input(f'Please enter the temperature in {tem}:')
if tem=='Fahrenheit':
    tem2=(float(temperature)-32)*5/9
    change='Celcius'
elif tem=='Celcius':
    tem2=(float(temperature)*9/5)+32
    change='Fahrenheit'
print(f'The temperatrue in {change} is {tem2}')
