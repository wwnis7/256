### if 문 [문제1]
# a = "Life is too short, you need python"
# if 'wife' in a:
#     print('wife')
# elif 'python' in a and 'you' not in a:
#     print('python')
# elif 'shirt' not in a:
#     print('shirt')
# elif 'need' in a:
#     print('need')
# else:
#     print('none')

### while 문
## 문제1
# i = 0
# s = 0
# while i < 1000:
#     i += 1
#     if i % 3 == 0: s += i
#     else: continue
# print(s)

## 문제2
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# a = 0
# s = 0
# while a in range(len(A)):
#     if A[a] >= 50: s += A[a]
#     else: pass
#     a += 1
# print(s)

## 문제3
# a = ''
# while 1:
#     a += '*'
#     print(a)
#     if len(a) == 4: break

### for 문
## 문제1
# for i in range(100):
#     print(i+1)

## 문제2
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# s = 0
# for x in A:
#     s += x
# print(f'mean is {s / len(A)}.')

## 문제3
# numbers = list(i + 1 for i in range(5))
# result = list()
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# print(result)

### 그냥 해본 문제
# def dict(**x):
#     return x                  # print(x)
# print(dict(a=1, b=2, c='s'))                                          #return과 print 구분하기. 함수의 값은 return이다. print(시행)가 있어도 함수의 값(return)이 없을 수 있다. 점프투파이선 참조.

### 함수
## 문제1
# def discriminator(x):
#     if x % 2 == 0: print(f'{x} is even.')
#     elif x % 2 == 1: print(f'{x} is odd')
# discriminator(3)

## 문제2
# def mean(*A):
#     s = 0
#     for x in A:
#         s += x
#     return s / len(A)
# print(mean(2,3,4,5,6))

## 책 문제1
# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fib(n-1) + fib(n-2)
# for i in range(20):
#     print(fib(i))

### 사용자 입력과 출력
## 문제1
# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")
# total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다" % total)

## 문제2
# a = input('Enter the numbers')
# A = a.split(',')
# s = 0
# for x in A:
#     s += int(x)
# print(s)

## 문제3
# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you", "need", "python")
# print("".join(["you", "need", "python"]))

## 문제4
# a = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
# print(' '.join([str(a*(x+1)) for x in range(9)]))

### 파일 읽고 쓰기
## 문제1
# f1 = open("C:/Users/wwnis/Desktop/ex/test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("C:/Users/wwnis/Desktop/ex/test.txt", 'r')
# print(f2.read())

## 문제2
# f1 = open("C:/Users/wwnis/Desktop/ex/test.txt", 'a')
# while 1:
#     data = input('저장할 내용을 입력하세요: ')
#     if not data: break
#     f1.write('\n'+data)
# f1.close()
# f2 = open("C:/Users/wwnis/Desktop/ex/test.txt", 'r')
# print(f2.read())

## 문제3
# with open("C:/Users/wwnis/Desktop/ex/test.txt", 'w') as f:
#     f.write('''AAA
# BBB
# CCC
# DDD
# EEE''')
# with open("C:/Users/wwnis/Desktop/ex/test.txt", 'r') as f:
#     lines = f.read()
# A = lines.split('\n')
# A.reverse()
# f = open("C:/Users/wwnis/Desktop/ex/test.txt", 'w')
# for i in A:
#     f.write(i)
#     f.write('\n')
# f.close


## 문제4
# with open("C:/Users/wwnis/Desktop/ex/test.txt", 'w') as f:
#     f.write('''Life is too short
# you need java''')
# with open("C:/Users/wwnis/Desktop/ex/test.txt", 'r') as f:
#     data = f.read()
# f = open("C:/Users/wwnis/Desktop/ex/test.txt", 'w')
# f.write(data.replace('java', 'python'))
# f.close

## 문제5
# with open("C:/Users/wwnis/Desktop/ex/test.txt", 'w') as f:
#     f.write('''70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100''')
# s = 0
# with open("C:/Users/wwnis/Desktop/ex/test.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         s += int(line.strip())
#     mean = s / len(lines)
# f = open("C:/Users/wwnis/Desktop/ex/result.txt", 'w')
# for line in lines:
#     f.write(line)
# f.write(f'\ntotal: {s}\nmean: {mean}')
# f.close

### 클래스
## 문제1
# class UpgradeCalculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val
#     def minus(self,val):
#         self.value -= val
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)

## 문제2
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val
# class MaxLimitCalculator(Calculator):
#     def add(self,val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
# cal = MaxLimitCalculator()
# cal.add(50)  # 50 더하기
# cal.add(60)  # 60 더하기
# print(cal.value)  # 100 출력

## 책 문제1
# class Calculator:
#     def __init__(self, list):
#         self.list = list
#     def sum(self):
#         sum = 0
#         for x in self.list:
#             sum += x
#         return sum
#     def avg(self):
#         return self.sum() / len(self.list)
# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.avg())
# cal2 = Calculator([6,7,8,9,10])
# print(cal2.sum())
# print(cal2.avg())

### 모듈 (위키닥스 문제 생략)
## 책 문제1
# from calculator import Calculator
# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.avg())

### 예외처리
## 문제1
# result = 0
# try:
#     [1, 2, 3][3]
#     "a"+1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4
# print(result)                       # 3 + 4

### 내장함수
## 문제1~6
# print(all([1, 2, abs(-3)-3]))
# print(chr(ord('a')) == 'a')
# print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))
# print(hex(234))
# print(int('0xea',16))
# print(list(map(lambda x:3*x, [1, 2, 3, 4])))
# print(round(17 / 3, 4))

### 외장함수
## 문제1
# import sys
# result = 0
# for x in sys.argv[1:]:
#     result += int(x)
# print(result)

## 문제2
# import os
# os.chdir('C:/Users/wwnis/.PyCharmCE2018.2/config/scratches')
# result = os.popen("dir")
# print(result.read())

## 문제3
# import glob
# print(glob.glob('C:/Users/wwnis/.PyCharmCE2018.2/config/scratches/*.py'))

## 문제4
# import time
# print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime((time.time()))))

## 문제5
# import random
# print(list(random.randint(1,45) for i in range(6)))