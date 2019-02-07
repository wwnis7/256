print('Please answer by pressing y or n')

Key = input('Is the car silent when you turn the key? ')






if Key == 'y':
    BT = input('Are the battery terminals corroded? ')
    if BT == 'y':
        print('Clean terminals and try starting again.')
    else :
        print('Replace cables and try again.')
else :
    CN = input('Does the car make a clicking noise? ')
    if CN == 'y':
        print('Replace the battery.')
    else:
        FS = input('Does the car crank up but fail to start? ')
        if FS =='y':
            print('Check spark plug connections.')
        else:
            ED = input('Does the engine start and then die? ')
            if ED =='n':
                print("Call the car center.")
            else:
                FI = input('Does your car have fuel injection? ')
                if FI =='y':
                    print('Get it in for service.')
                else:
                    print('Check toen sure the choke is opening and closing')