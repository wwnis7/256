
age=input('What is your current age? ')
retire=input('At what age would you like to retire? ')
left=int(retire)-int(age)
year=input('year?')
yearint=int(year)
year2=int(year)+left
print('You have %d years left until you can retire'%left)
print('It\'s %d, so you can retire in %d.'%(yearint,year2))

#int(year)한번해두면 인트형된거아닌가?
