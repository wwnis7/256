# TargetHeartRate = (((220 − age) − restingHR) × intensity) + restingHR

age = input('age: ')
rHR = input('restingHR: ')
intensity = 55

while intensity >= 55:
    THR = (((220 - float(age)) - float(rHR)) *intensity/100) + float(rHR)
    print(THR)
    intensity += 5
    if intensity == 100:
        break
