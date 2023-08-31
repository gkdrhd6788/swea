arr = 'ABC'
N = len(arr)
bits = [0]*N
for i in range(2):
    bits[0]=i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2]= k
            print(bits)