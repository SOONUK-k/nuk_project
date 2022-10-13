from bisect import bisect_right


test={'Korean':80, 'Enlgish':75, 'Math':55}
score=list(test.values())
print(score[1])
score2=list(test.keys())
c =0
print(bool(score))
while bool(score):
    c+=score.pop()

c = c / len(score2)
print(c)


num =13
print(num%2)
while num%2:
    print("%d 는 홀수입니다" %num)
    num=num+1

pin="881120-1068234"

pin_left = pin[0:6]
pin_right = pin[7:13]

print(pin_left)
print(pin_right)

print("홍길동씨의 주민등록의 생년월일은 19%s 이고 주민등록번호의 뒷자리는 %s이다 "  %(pin_left, pin_right))
print(pin_right[0])

Q5 = "a:b:c:d"
CQ5= Q5.replace(""":""","""#""")
print(CQ5)

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

Q6 = [1,3, 5, 4, 2]
Q6.sort()
Q6.reverse()
print(Q6)

Q7=['Life', 'is', 'too', 'short']
reQ7=" ".join(Q7)
print(reQ7)

Q8=(1, 2, 3)
reQ8=(4,)
what = Q8 + reQ8
print(what)
