# 부분집합
arr = [3,6,7,1,5,4]
N = 6
for i in range(1<<N):
    subset1=[]
    for j in range(N):  # 원ㅅ의 수만큼 비트를 비교(질문)
        if i & (1<<j):
            subset1.append(arr[j])
    print(subset1)

# 두개의 부분집합
arr = [3,6,7,1,5,4]
N = 6
for i in range(1<<N):
    subset1=[]
    subset2=[]
    for j in range(N):  # 원ㅅ의 수만큼 비트를 비교(질문)
        if i & (1<<j):
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1,subset2)

# 공집합 제외
arr = [3,6,7,1,5,4]
N = 6
for i in range(1,(1<<N)-1 ): # 괄호 쳐야
    subset1=[]
    subset2=[]
    for j in range(N):  # 원ㅅ의 수만큼 비트를 비교(질문)
        if i & (1<<j):
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1,subset2)


# 공집합 제외 & 중복 제외
arr = [3,6,7,1,5,4]
N = 6
for i in range(1,(1<<N)//2 ): # 괄호 쳐야  # 1<<(N-1)로 해도 동일
    subset1=[]
    subset2=[]
    for j in range(N):  # 원ㅅ의 수만큼 비트를 비교(질문)
        if i & (1<<j):
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1,subset2)