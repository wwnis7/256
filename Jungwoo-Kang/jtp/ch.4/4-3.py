#f1 = open("test.txt", 'w')
#f1.write("Life is too short")
#f1.close()
#f2 = open("test.txt", 'r')
#data=f2.read()
#print(data)

#2
#f = open("22.txt",'a')
#f.write(input()+"\n")
#f.close

#3
#f = open("33.txt",'w')
#f.write("AAA\nBBB\nCCC\nDDD\nEEE")
#f.close()

#f = open("33.txt", 'r')
#lines = f.readlines()
#while 1:
#    if lines is 0:
#        break
#    else:
#        print(lines.pop())
#f.close()

#위에건 왜 에러가 뜨지

#3
#f = open("33.txt",'w')
#f.write("AAA\nBBB\nCCC\nDDD\nEEE")
#f.close()

#f = open('33.txt', 'r')
#lines = f.readlines()  # 모든 라인을 읽음
#f.close()

#lines.reverse()  # 읽은 라인을 역순으로 정렬

#f = open('33.txt', 'w')
#for line in lines:
#    line = line.strip()  # 포함되어 있는 줄바꿈 문자 제거
#    f.write(line)
#    f.write('\n')  # 줄바꿈 문자 삽입
#f.close()

#4
#f = open("44.txt",'w')
#f.write("Life is too short.\nyou need java.")
#f.close()

#f = open('44.txt', 'r')
#body = f.read()
#f.close()


#body = body.replace('java', 'python')

#f = open('44.txt', 'w')
#f.write(body)
#f.close()

#5
f=open("55.txt",'w')
f.write("70\n65\n80\n90\n75\n55\n45\n60\n40\n35\n")
f.close()

sum=0
f=open("55.txt",'r')
lines= f.readlines()
    for line in lines:
        sum+=int(line)

avg=sum/len(lines)

f=open("55b.txt",'w')
f.write(str(avg))
f.close()

#왜 안될까..