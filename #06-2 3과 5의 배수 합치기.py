#06-2 3과 5의 배수 합치기
"""
num = range(1,11)
print(num[0])
print(num[9])

i=1
box=0
while i<1000:
    if i%3==0:
        box+=i
        i+=1
    elif i%5==0:
        box +=i
        i+=1
    else:
        i+=1

print(box)



result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: 
        result += n
print(result)
"""
"""
#06-3 게시판 페이징하기
fw = open("memo.txt",'w')
fr = open("memo.txt",'r')
fa = open("memo.txt",'a')
number = input("If you want to append then type'1' \n No! I want to read only then type'2': ")

if number==1:
    data = input("Please type ur content here: ")
    fa.write(data)
    fa.write('\n')
    fa.close()
elif number==2:
    data2 = fr.read()
    fr.close()
    print(data2)
else:
    print("You typed wrong word here")
"""
#05 make a tab as four blank space