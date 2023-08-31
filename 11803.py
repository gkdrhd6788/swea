import copy
def f(i,M):
    if i ==M:
        #p1= copy.deepcopy(p) #여기서 배터리 사용량을 바로 계산하면 더 빠름(강사님 코드 메타모스트 참고-가지치기까지)
        case.append(p)
        print(p)
        return
    else:
        for j in range(M):    # 0,1
            if used[j] == 0: #if used[j]==1: continue하는 것도 익히기
                p[i] = office[j]  #여기서 j 로 하면 되었던 것
                used[j] = 1
                f(i+1,M)
                used[j] = 0

# for tc in range(1,int(input())+1):
case=[]
N = int(input()) # 관리구역 갯수+1, 3
M = N-1 # 관리구역 갯수,2
office = [i for i in range(2,N+1)] #2,3  #이렇게 줄 필요없었음..(11번줄)
used=[0]*M  #[0,0]
p=[0]*M  #[0,0]
arr=[list(map(int,input().split())) for _ in range(N)]


f(0,M)
print(case)
min_battery = 100*N
for route in case:
    battery = 0
    for i in range(M-1):
        battery += arr[route[i]-1][route[i+1]-1]
    battery += arr[1-1][route[0]-1]+arr[route[-1]-1][1-1]
    if min_battery>battery:
        min_battery = battery
print(min_battery)
# print(f'#{tc} {min_battery}')