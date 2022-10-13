#Q1

def is_odd(a):
    if a%2==0:
        print("%dis odd" %a)
    else:
        print("%dis not odd" %a)
is_odd(3)


def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
     result = 0
     for i in args:
         result += i
     return result / len(args)


#Q2
def makemean(*args):
    result=0
    for i in args:
        result += i
    
    return result/len(args)
    
#Q5
f1=open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2=open("test.txt",'r')
line=f2.readlines()
f2.close()
print(line)

Q6=open("test.txt", 'a')
num = input("type number: ")
Q6.write(num)
Q6.close()