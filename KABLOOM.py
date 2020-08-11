def add(a,b):
    if(a == 'R' and b == 'R'):
        return 50
    if(a == 'R'):
        if(b == 'A'): return 20
        if(b == 'Q'): return 15
        if(b == 'K'): return 15
        if(b == 'J'): return 15
        if(b == 'T'): return 10
        return int(b)
    if (b == 'R'):
        if (a == 'A'): return 20
        if (a == 'Q'): return 15
        if (a == 'K'): return 15
        if (a == 'J'): return 15
        if (a == 'T'): return 10
        return int(a)
    if (a == 'A'): return 20
    if (a == 'Q'): return 15
    if (a == 'K'): return 15
    if (a == 'J'): return 15
    if (a == 'T'): return 10
    return int(a)
result_list = []
N = int(input())
memorization = [[0] * (1001) for i in range(1001)]
while(N != 0):
    a = input().split(" ")
    b = input().split(" ")
    for i in range(1,N+1):
        for j in range(1,N+1):
            memorization[i][j] = max(memorization[i-1][j],memorization[i][j-1])
            if(a[i-1] == b[j-1] or a[i-1]=='R' or b[j-1] == 'R'):
                memorization[i][j] = max(memorization[i][j],memorization[i-1][j-1] + add(a[i-1],b[j-1]))
    result_list.append(memorization[N][N] * 2)
    N = int(input())
for li in result_list:
    print(li)

