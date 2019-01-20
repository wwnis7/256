# p106
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# p106
pin = "881120-1068234"
print(pin[7])

# p107
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

# p107
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# p108
a = (1,2,3)
a = a + (4,)
print(a)

# 02-1
국어 = 80
영어 = 75
수학 = 55
A = [국어, 영어, 수학]
mean = sum(A) / len(A)
print(mean)

# 02-1
a = int(input('Enter a natural number'))
D = {0:'Even', 1:'Odd'}
print(D[a%2])

# 02-2
print('a:b:c:d'.replace(':', '#'))
print('#'.join('a:b:c:d'.split(':')))

# 02-2
A = ['Life', 'is', 'too', 'short']
print(' '.join(A))

# 02-3
B = [1,3,5,4,2]
B.sort()
B.reverse()
print(B
