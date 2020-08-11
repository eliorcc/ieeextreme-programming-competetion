def find(parent,x):
    if(parent[x] < 0):
        px = x
    else:
        px = find(parent,parent[x])
        parent[x] = px
    return px

def union(parent,x,y):
    px = find(parent,x)
    py = find(parent,y)
    if(px != py):
        if(parent[px] < parent[py]):
            parent[px] += parent[py]
            parent[py] = px
        else:
            parent[py] += parent[px]
            parent[px] = py
def legal(x,y,H):
    return (x >= 1 and x <= H) and (y >= 1 and y <= H)
def pos2Index(x,y,H):
    return (x-1) * H + (y-1)

H = int(input())
parent = [-1] * (H*H+2)

maze = [[0] * (H+2) for i in range(H+2)]
for i in range(1,H+1):
    union(parent,pos2Index(1,i,H),H*H)
    union(parent,pos2Index(H,i,H),H*H+1)
d = []
d.append([0,1])
d.append([0,-1])
d.append([1,0])
d.append([-1,0])
count = 1
while(1):
    input1 = input()
    if (input1 == '-1'):
        print(-1)
        break
    input_list = input1.split(" ")
    x = int(input_list[0])
    y = int(input_list[1])
    maze[x][y] = 1
    for li in range(4):
        nx = x + d[li][0]
        ny = y + d[li][1]
        if(legal(nx,ny,H) and maze[nx][ny]):
            union(parent,pos2Index(x,y,H),pos2Index(nx,ny,H))

    if(find(parent,H*H) == find(parent,H*H+1)):
        print(count)
        break
    count += 1
