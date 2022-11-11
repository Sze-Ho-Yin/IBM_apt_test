N = int(input())

err_msg = {}
for i in range(N):
    msg = list(map(str, input().split()))
    if msg[1] == 'false':
        err_msg[msg[2]] = 0
err_msg_list = list(err_msg.keys())
if len(err_msg)==0:
    print("Yes")
else:
    print("No")
    for i in err_msg_list:
        print(i, end=' ')
    