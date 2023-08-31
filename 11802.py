for tc in range(1,int(input())+1):
    arr = list(map(int,input().split())) # 모든 카드  12개
    player1 = []
    player2 = []
    for i in range(12):
        if i%2==0:
            player1.append(arr[i])
        else:
            player2.append(arr[i])

    flag = False
    win_index1 = 20 # 10보다 큰 값을 줘야함
    cnt1=[0]*12
    for j in range(6):
        cnt1[player1[j]]+=1
        for k in range(10):
            if cnt1[k]>=3:
                win_index1=j*2  # 둘다 찾은경우 1이 이기기 위해
                flag= True
                break
            elif cnt1[k]>=1 and cnt1[k+1]>=1 and cnt1[k+2]>=1:
                win_index1 = j*2
                flag = True
                break
        if flag: break


    flag2 = False
    win_index2 = 20
    cnt2=[0]*12
    for q in range(6):
        cnt2[player2[q]]+=1
        for w in range(10):
            if cnt2[w]>=3:
                win_index2=q*2+1
                flag2= True
                break
            elif cnt2[w]>=1 and cnt2[w+1]>=1 and cnt2[w+2]>=1:
                win_index2 = q*2+1
                flag2 = True
                break
        if flag2: break

    if win_index1 > win_index2:
        result = 2
    elif win_index1==win_index2:
        result = 0
    else:
        result = 1
    print(f'#{tc} {result}')