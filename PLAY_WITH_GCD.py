mod = 10**9 + 7
maxn = 100005
def add(x,y):
    x+=y
    if(x>=mod):
        x-=mod
    return x
