# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i,N,key,arr):
    if i ==N:
        return 0 #key가 없는 경우
    elif arr[i]==key:
        return 1
    else:
        return f(i+1,N,key,arr) #return안적으면 None이 나오는 이유

N = 5
A = [1,2,3,4,5]

key = 3
print(f(0,N,key,A))