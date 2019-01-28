# person’s height in inches and weight
# in pounds. The program should prompt the user for weight
# and height.
# Calculate the BMI by using the following formula:
# bmi = (weight / (height × height))* 703

height=input('height in inches: ')
weight=input('weight in pounds: ')
BMI=(float(weight)/pow(float(height),2))*703

print(f'Your BMI is {BMI}.')
if BMI>25:
    print('you are overweight. You should see your doctor.')
elif BMI<18.5:
    print('yor are underweight. You should see your doctor.')
else:
    print('You are within the ideal weight range.')