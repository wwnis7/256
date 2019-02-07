n=5
i=0
total=0
sum=[]
while i < 5:

    a=input('Enter a number: ')
    sum.append(a)
    total+=int(sum[i])
    i+=1
print(total)