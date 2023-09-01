N , M = map(int,input().split()) # N*M 크기
arr = [list(input()) for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'W' : continue
def BFS(n):
    queue.append(n)
    visited[ ] =1
    while queue:
        t = queue.pop(0)
        print(t)
        for w in [[0,1],[1,0],[0,-1],[-1,0]]:
            
