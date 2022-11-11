def transform(l) -> list:
    temp = []
    for i in l:
        val = 0
        if i[len(i)-1]=='L':
            val = 1*(len(i))
        elif i[len(i)-1]=='S':
            val = -1*(len(i))
        temp.append(val)
    temp.sort(reverse=True)
    return temp

N = int(input())
avail = list(map(str, input().split()))
M = int(input())
req = list(map(str, input().split()))

if M>N:
    print("No")
else:
    avail = transform(avail)
    req = transform(req)
    flag = True
    for i in range(M):
        if (avail[i]<req[i]):
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")



