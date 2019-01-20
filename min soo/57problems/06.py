from datetime import datetime
try:
    age = int(input('What is your current age? '))
    retire = int(input('At what age would you like to retire? '))
    today = int(datetime.today().year)
except: print('Invalid')
left = retire - age
day = today + retire - age
if left >= 0:
    print(f"""You have {left} years left until you can retire.
It's {today}, so you can retire in {day}.""")
else: print('You already retired.')