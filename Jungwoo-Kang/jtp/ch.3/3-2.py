#1
a=0
b=0
while a<=1000:
    a+=1
    if a%3 == 0:
        b+=a
    else:
        continue
print(b)

#2
#$$A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
#c=0
#d=0
#while c<10:
   # if A[c] >= 50 :
  # c+=1
  #  else: continue
##이건 왜 안되는거지

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
c=0
while A:
    if A.pop() >=50:

        c+=A.pop()
    else: continue
print(c)

# A.pop()을 변수로 잡고 하면 되는데 왜 위처럼 하면 답이 다르게 나올까 --- A.pop을 할때마다 하나씩 빠지므로 누락

#3
c=1
while c<5:
    print("*"*c)
    c+=1

