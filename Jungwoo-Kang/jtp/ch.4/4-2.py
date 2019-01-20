#1
#input1 = input("첫번째 숫자를 입력하세요:")
#input2 = input("두번째 숫자를 입력하세요:")


#total = float(input1) + float(input2)
#print("두 수의 합은 %f 입니다" % total)

#2
#user_input = input("숫자를 입력하세요:")
#numbers = user_input.split(",")
#total = 0
#for n in numbers:
   # total += int(n)  # 입력은 문자열이므로 숫자로 변환해야 한다.
#print(total)
#print(numbers)

#4
input_num=input("구구단을 실행할 숫자를 2~9까지 입력하시오.")
a=[int(input_num)*i for i in range(1,10)]
print(a)