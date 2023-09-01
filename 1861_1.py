for tc in range(1, int(input())+1):
    N = int(input())  # 행렬 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열
    max_start = 0
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            flag = True
            ii, jj = i, j
            while flag:
                num = arr[ii][jj]
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = ii + di, jj + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == num + 1:
                            ii, jj = ni, nj
                            cnt += 1
                            break
                else:
                    flag = False
            if max_cnt < cnt:
                max_cnt = cnt
                max_start = arr[i][j]
            elif max_cnt == cnt:
                max_start = min(max_start, arr[i][j])

    print(f'#{tc} {max_start} {max_cnt}')



