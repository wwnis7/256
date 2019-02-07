# Enter a name: Homer
# Enter a name: Bart
# Enter a name: Maggie
# Enter a name: Lisa
# Enter a name: Moe
# Enter a name:
# The winner is... Maggie.
List=[]
name=''
while name != 'exit':
    name=input('Enter a name: ')
    List.append(name)
#random으로 len(List)까지 n 생성
n=3
print(f'The winner is... {List[n]}.')