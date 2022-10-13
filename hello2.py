
n = int(input())

list1= range(1,n+1)
list2=[]
for i in range(n):
    A = int(input())
    list2.append(A)



i=0
j=0
wrong=0
result=[]
result_value=[]
chk_value=[]

while True:   
    if chk_value ==list2:
        break
    elif i  == n:
        if result_value[len(result_value)-1] == list2[j]:
                result.append("-")
                chk_value.append(list2[j])
                result_value.pop()
                j+=1
        else:
            wrong+=1
            break

    if (i<n and list2[j]>list1[i]):
        result.append("+")
        result_value.append(list1[i])
        i+=1
    elif (i<n and list2[j]==list1[i]):
        result.append("+")
        result.append("-")
        chk_value.append(list1[i])
        i+=1
        j+=1
    elif (i<n and list2[j]<list1[i]):
            if result_value[len(result_value)-1] == list2[j]:
                result.append("-")
                chk_value.append(list2[j])
                result_value.pop()
                j+=1
            else:
                wrong+=1
                break
if wrong != 0:
    print("NO")
else:
    for i in result:
        print(i)