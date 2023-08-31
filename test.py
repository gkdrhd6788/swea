def dfs(n,m,V,adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    # do something
    while True:
        for w in range(1,V+1): # +1 맞나?
            if adj_m[n][w] ==1 and visited[w]==0 :
                if w != m:
                    stack.append(n)
                    n = w
                    # do something
                    visited[n]=1
                    break
                else:
                    return 1
        else:
            if stack:
                n= stack.pop()
            else:
                return 0

# for tc in range(1, int(input())+1):
V, E = map(int,input().split())
adj_m = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    i,j = map(int,input().split())
    adj_m[i][j] = 1  # 시작점i이 행, 끝점j이 열  , 방향성이므로 1개만
#print(adj_m) # 잘 나옴
S,G = map(int,input().split()) # 출발 노드 S와 도착노드 G

print(dfs(S,G,V,adj_m))