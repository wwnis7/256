a=[1,2,3]
b=[1,2,3]
print(bool(a is b))

##id 가 다름

c=[1,2,3]
print(id(c))
c=c+[4,5]
print(id(c))

d=[1,2,3]
print(id(d))
d.extend([4.5])
print(id(d))

print(bool(c is d))

##근데 왜 아이디는 같은데 다르다고 나오지?