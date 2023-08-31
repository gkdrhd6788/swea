#dfs연습_인접리스트 버전
def dfs(n,V,adj_m,f):
    stack = [] # 스택 생성
    visited = [0]*(V+1) # 방문정보리스트 생성
    visited[n] = 1 # 시작점 방문 표시
    while True:
        if n==f:
            return 1
        for w in adj_m[n]: # 인접리스트에 있는 값만 순회!!(효율)
            if visited[w]==0: # 위에서 한번 걸러줬으므로 이 조건만 탐색하면 됨
                stack.append(n)  #시작점 append하기
                n = w     # n에 w 지정하기     (이전에 할일 1개  이후에 할일 2개)
                visited[n] =1 # 방문표시하기
                #print(n)  #프린트
                break    # for문 중단
        else:  # for문을 돌아도 if 를 만족하는 것이 없어서 break되지 않은 경우(즉, 인접이 없거나 모두 방문한 경우)
            if stack:
                n = stack.pop()  #마지막에 지나온 정점을 n으로 해서 다시 while문 돌림
            else: #스택이 비어있음
                break # while문 중단
    return 0

for tc in range(1, int(input())+1):
    V,E = map(int,input().split()) #V개 이내의 노드, E개의 간선
    adj_m = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj_m[s].append(e)
    #print(adj_m)
    start,finish = map(int,input().split())
    print(f'#{tc} {dfs(start,V,adj_m,finish)}')



