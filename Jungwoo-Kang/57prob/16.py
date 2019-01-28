# What is your age? 15
# You are not old enough to legally drive.
# Or
# What is your age? 35
# You are old enough to legally drive.

age=input('what is your age?')

if int(age)<16:
    print('You are not old enough to legally drive.')
else:
    print('You are old enough to legally drive.')
