#1
p=[]
for i in range(100):
    p.append(i)
print(p)
    #print(i+1,end=' ')

#2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total=0
for number in A:
    total+=number
    continue
avg=total/len(A)
print(avg)

#3
numbers = [1, 2, 3, 4, 5]
odd=[i*2 for i in numbers if i%2==1 ]
print(odd)