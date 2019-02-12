length=input('length? ')
width=input('input? ')
area=int(length)*int(width)
gallons=round(float(area)/350)
if area%350 ==0:
    gallons = round(float(area) / 350)
else:
    gallons = round(float(area) / 350)+1

print('''You will need to purchase %d gallons of
paint to cover %d square feet.'''%(gallons,area))
