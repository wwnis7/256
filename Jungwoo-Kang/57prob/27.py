def VI():
    sum=0
    firstname = input('Enter the first name: ')
    lastname = input('Enter the last name: ')
    zipcode = input('Enter the zip code: ')
    id = input('Enter an employee ID: ')

    if len(firstname) <= 1:
        print(f'{firstname} is not a valid first name. It is too short.')
    else:
        sum+=1

    if len(lastname) <= 1:
        print(f'{lastname} is not a valid last name. It is too short.')
    else:
        sum+=1

    try:
        numeric_zip = int(zipcode)
        sum+=1
    except:
        print('The zip code must be numeric.')

    if ord(id[0]) >= 65 and ord(id[0]) <= 90 and ord(id[1]) >= 65 and ord(id[1]) <= 90:
        if id[2] == '-':
            e=0
            for i in id[3:]:
                if ord(i) >= 48 and ord(i) <= 57:
                    e+=1
                else:
                    continue
            if e==4 and len(id[3:])==4 :
                sum+=1
            else:
                print(f'The {id} is not a valid ID.')
        else:
            print(f'The {id} is not a valid ID.')
    else:
        print(f'The {id} is not a valid ID.')

    if sum==4:
        print('There were no errors found.')
VI()
