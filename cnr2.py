def subset(i,N):
    if i == N:
        s = 0 #부분집합의 합
        for j in range(N):
            if bit[j] : #
                s = arr[j]
        if s ==0:  #0이되는 경우 출력(-3,3..)
            for j in range(N):
                if bit[j]:
                    print(arr[j],end = '')
            print()

    else:
        bit[i] = 1
        subset(i+1,N)
        bit[0]
        subset(i + 1, N)

def subset(i,N,s):
    if i == N:
        if s ==0:  #0이되는 경우 출력(-3,3..)
            for j in range(N):
                if bit[j]:
                    print(arr[j],end = '')
            print()

    else:

        subset(i+1,N,s+arr[i])
        subset(i + 1, N,s)

arr = [-1,3,-9,6,7-6, ,5,4,-2]
