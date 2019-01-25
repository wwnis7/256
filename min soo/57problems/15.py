import getpass
A = {'id1': 'pw1', 'id2': 'pw2', 'id3': 'pw3'}

a = input('Write your id')

def f(x,y):
    A[x] = y
    print('You create your account.')


if a not in A:
    print('There is no account like that')
    while 1:
        a = input('Do you want to join us? y/n')
        if a in ['y', 'n']:
            if a == 'y':
                while 1:
                    x = input('Enter your id')
                    if x in A:
                        print('This id already exists')
                    else:
                        print('You can use this id')
                        break
                while 1:
                    y = input('Enter your pw')
                    y_1 = input('Repeat your password.')
                    if y == y_1: break
                    else: print('Does not correct.')
                f(x, y)
                break
            else:
                print('Goodbye!')
                break
        else:
            print('Invalid.')
else:
    pw = input('What is your password: ')
    if pw == A[a]:
        print('Welcome!')
    else:
        print('That password is incorrect.')

# a = input('Write your id')
#
#
# if a not in A:
#     print('There is no account like that')
# else:
#     pw = input('What is your password: ')
#     if pw == A[a]:
#         print('Welcome')
#     else:
#         print('That password is incorrect.')
