# print(f"Hello, {input('What is your name?')}, nice to meet you!")

a = input('Select your language. Eng, Kor, or jpn')
if a.upper() == 'Eng'.upper():
    print(f'Hello, {input("What is your name?")}, nice to meet you!')
elif a.upper() == 'Kor'.upper():
    print(f'{input("당신의 이름은?")}, 안녕? 만나서 만가워!')
elif a.upper() == 'jpn'.upper():
    print(f'{input("What is your name?")}상, 곤니치와!')
else: print('Invalid')
