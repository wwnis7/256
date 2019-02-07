# What's the minimum length? 8
# How many special characters? 2
# How many numbers? 2
# Your password is
# aurn2$1s#

minimum = input('WHat\'s the minimum length? ')
maximum = input('WHat\'s the maximum length? ')
min = int(minimum)
max = int(maximum)

if max < min:
    print('Minimum length is longer than maximum!!')

num_number = input('How many numbers? ')
num_special_character = input('How many special character? ')

number = '0123456789'
special_character = '~!@#$%^&*()-=+_'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

sub = max - min
range(sub)  # 여기서 랜덤으로 숫자하나 셀렉 n으로

password_length = min + sub
len(password_length)  # 여기에서 num_number+num_special_character 만큼 랜덤으로 선택
# num_special+num_special_character length에서 num_special 만큼 랜덤으로 선택후 위 랜덤선택 리스트에서 그index선택해서
# j로 지칭 아닌 애들은 k로 지칭
i = 0
while i <= password_length:

