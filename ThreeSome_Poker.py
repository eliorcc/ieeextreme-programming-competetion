import math
input_list = (input()).split(" ")
#x = player1 money
#y = player2 money
#z = player3 money
x = input_list[0]
y = input_list[1]
z = input_list[2]
counter = 0
store_values = [[-1]*3 for i in range(797161)]
store_values[0][0] = x
store_values[0][1] = y
store_values[0][2] = z
first_0_index = -1
indexes = []
for i in range(797161):
    for j in range(3):
        store_values[i][j] = int(store_values[i][j])
for i in range(int((797161/3))):
    if (store_values[i][0] == 0 or store_values[i][1] == 0 or store_values[i][2] == 0):
        first_0_index = i
        break
    if((store_values[i][0]) > (store_values[i][1])):
        store_values[(3*i) + 1][0] = (store_values[i][0] - store_values[i][1])
        store_values[(3*i) + 1][1] = (2*store_values[i][1])
        store_values[(3*i) + 1][2] = (store_values[i][2])
    if((store_values[i][0]) <= (store_values[i][1])):
        store_values[(3*i) + 1][0] = (2*store_values[i][0])
        store_values[(3*i) + 1][1] = (store_values[i][1] - store_values[i][0])
        store_values[(3*i) + 1][2] = (store_values[i][2])
    if((store_values[i][0]) > (store_values[i][2])):
        store_values[(3*i) + 2][0] = (store_values[i][0] - store_values[i][2])
        store_values[(3*i) + 2][1] = (store_values[i][1])
        store_values[(3*i) + 2][2] = (2*store_values[i][2])
    if((store_values[i][0]) <= (store_values[i][2])):
        store_values[(3*i) + 2][0] = (2*store_values[i][0])
        store_values[(3*i) + 2][1] = (store_values[i][1])
        store_values[(3*i) + 2][2] = (store_values[i][2] - store_values[i][0])
    if ((store_values[i][1]) > (store_values[i][2])):
        store_values[(3 * i) + 3][0] = (store_values[i][0])
        store_values[(3 * i) + 3][1] = (store_values[i][1] - store_values[i][2])
        store_values[(3 * i) + 3][2] = (2*store_values[i][2])
    if ((store_values[i][1]) <= (store_values[i][2])):
        store_values[(3 * i) + 3][0] = (store_values[i][0])
        store_values[(3 * i) + 3][1] = (2*store_values[i][1])
        store_values[(3 * i) + 3][2] = (store_values[i][2] - store_values[i][1])

if(first_0_index == -1):
    print('Ok')
else:
    while(first_0_index >= 0):
        indexes.append(first_0_index)
        first_0_index = int(math.floor((first_0_index-1.0)/3))
    len1 = len(indexes)
    indexes = indexes[::-1]
    for i in indexes:
        print('{0} {1} {2}'.format(store_values[i][0],store_values[i][1],store_values[i][2]))


