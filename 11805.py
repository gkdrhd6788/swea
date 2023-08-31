for tc in range(1,int(input())+1):
    N=int(input()) # 신청서 갯수
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    #print(arr)
    arr.sort(key=lambda x : x[1])
    arr = [ [0,0]] + arr
    #print(arr)
    S = []
    j = 0

    for i in range(1,N+1):
        if arr[i][0] >= arr[j][1]:
            S.append(i)
            j = i

    print(f'#{tc} {len(S)}')