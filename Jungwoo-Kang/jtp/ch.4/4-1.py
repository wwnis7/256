#1
def is_odd(a):
    if a%2 ==0:
        print("%d는 짝수입니다."%a)
    else:
        print("%d는 홀수입니다."%a)

is_odd(3)

#2
def sum(*args):
    sum=0
    n=0
    for i in args:
        sum +=i
        n+= 1
    avg=sum/n
    print(args)
    print("의 평균은 %f입니다."%avg)


sum(1,2,3,4)

#print 두개 같은줄에 쓸수 있는 방법은 없나?





