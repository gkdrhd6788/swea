N = int(input())  # 행렬 크기
arr =  [ list(map(int,input().split())) for _ in range(N) ] # 배열
max_start = 0
max_cnt = 0
for i in range(N):
    for j in range(N):
        cnt = 1
        flag = True
        while flag:

            num = arr[i][j]
            for di,dj in [ [0,1],[1,0],[0,-1],[-1,0] ]:
                ni , nj = i + di , j + dj
                if 0 <= ni < N and 0 <= nj < N :
                    if arr[ni][nj] == num + 1 :
                        i, j = ni, nj
                        cnt += 1
                        break
            else:
                flag = False
        if max_cnt < cnt :
            max_cnt = cnt
            max_start = arr[i][j]
        elif max_cnt == cnt :
            max_start = min(max_start,arr[i][j])

print(max_start, max_cnt)



