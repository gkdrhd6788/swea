for tc in range(1,int(input())+1):
    N,M = map(int,input().split())  #N컨테이너 수, M트럭수
    weight = list(map(int,input().split())) # N컨테이너의 무게
    capacity = list(map(int,input().split())) # M 트럭의 적재 용량(기준)
    weight.sort(reverse = True)
    capacity.sort(reverse = True)

    total = 0
    for i in range(M): #M :트럭수(capacity 관련)
        for j in range(N): # N: 컨테이너 (weight관련)
            if capacity[i] >= weight[j]:
                total += weight[j]
                #weight.del(weight[j]) # 이렇게 하거나
                #del weight[j]    # 이렇게 하면 out of range에러 뜸.
                weight[j]=51      # 그래서 이렇게 값을 변경해줌
                break
    print(f'#{tc} {total}')

