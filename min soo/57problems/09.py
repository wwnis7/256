import math
D = {'square':1, 'circle':math.pi, 'l-shape':3/4}
c = 9
while 1:
    shape = input('Enter the shape. square, circle, or L-shape: ')
    if shape.lower() in D.keys():
        break
    else: print('Invalid.')
while 1:
    if shape.lower() == 'circle':
        r = input('Enter the radius: ')
        try:
            r = int(r)
            break
        except:
            try:
                r = float(r)
                break
            except: print('Invalid.')
    else:
        length = input('Enter the length: ')
        width = input('Enter the width: ')
        try:
            length, width = int(length), int(width)
            break
        except:
            try:
                length, width = float(length), float(width)
                break
            except: print('Invalid.')
if shape.lower() == 'circle': area = D[shape.lower()] * r ** 2
else: area = D[shape.lower()] * length * width
num = math.ceil(area/c)
print(f'You will need to purchase {num} liters of paint to cover the {area:.3f} square meters.')