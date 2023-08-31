def f(i,N):
    if i==N:
        print(p) #여기에 babyjin 판단코드 작성
        return
    else: #card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j]==0:
                p[i] = card[j]
                used[j]=1
                f(i+1,N)
                used[j]=0 #복구

card = list(map(int,input()))
used=[0]*(6)
p=[0]*6
f(0,6)

def f(i,N,K): # i는 이전에 고른 갯수, N개에서 K개를 고르는 순열
    if i==K:
        print(p) #여기에 babyjin 판단코드 작성>>>>
        return
    else: #card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j]==0:
                p[i] = card[j]
                used[j]=1
                f(i+1,N,K)
                used[j]=0 #복구

card = [1,2,3,4,5]
N = 5 # N개의 숫자에서
K = 3 # K개를 골라 만드는 순열
used=[0]*N
p=[0]*K
f(0,N,K)