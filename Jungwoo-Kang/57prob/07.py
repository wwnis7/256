

length=input('What is the length of the room in feet? ')
width=input('What is the width of the room in feet? ')
area=int(length)*int(width)
f_area=area*0.09290304
print('''you entered dimensions of %d feet by %d feet.
      The area is %d square feet
      %f square meters.'''%(int(length),int(width),area,f_area))
