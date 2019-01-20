c = 0.09290304
D = {'feet':'meter', 'meter':'feet'}
unit = input('Choose the unit you will enter: feet/meter')
while unit.lower() not in ['feet', 'meter']:
      unit = input('Invalid. Choose the unit you will enter: feet/meter')
while 1:
      length = input(f'What is the length of the room in {unit.lower()}')
      width = input(f'What is the width of the room in {unit.lower()}')
      try:
            length = int(length)
            width = int(width)
            break
      except:
            try:
                  length = float(length)
                  width = float(width)
                  break
            except: print('Invalid')
area = length*width
if unit.lower() == 'feet':
      area_2 = area * c
else:
      area_2 = area / c
print(f'''You enter the dimension {length} {unit.lower()} by {width} {unit.lower()}
The area is
{area} square {unit.lower()}
{area_2:.3f} square {D[unit.lower()]}''')
