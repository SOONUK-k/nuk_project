import sys

N = int(sys.stdin.readline())
li=[]
lia = [0]* 8001
for i in range(N):
    A = int(sys.stdin.readline())
    lia[A+4000]+=1
    li.append(A)
print(round(sum(li)/N))   #산술평균
li.sort()

print(li)

print(li[(N//2)])    #중앙값 출력
#####

x=max(lia)          #최빈값 index찾기
print(x)
xp = lia.index(x)   #최빈값 value(몇번)
print(xp)
lia[x]=1   #최반값 바꿔두기 1로

x2=max(lia)          #최빈값2 index찾기
print(x2)
xp2 = lia.index(x)   #최빈값2 value(몇번)
print(xp2)

if xp==xp2:
    print(x2-4000)
else:
    print(x-4000)


###
d1=0
d2=0
for i in range (8001):
    if(lia[i]!=0):
        d1=i
        break
T=8000
while T<8002:
    if (lia[T]==0):
        T -=1
    else:
        d2 = T
        break

print(d2-d1)     #범위출력
