square_size = int(input())
square_2d_array = [[0]*square_size for _ in range(square_size)]
for i in range(0,square_size):
    row = input()
    splitted_row = (row.split(" "))
    for j in range(0,square_size):
        square_2d_array[i][j] = int(splitted_row[j])
main_diagonal_size = sum(square_2d_array[i][i] for i in range(square_size))
antidiagonal_sum = sum(square_2d_array[i][square_size-i-1] for i in range(square_size))

list = []
if(main_diagonal_size != antidiagonal_sum):
    list.append(0)
#running on all rows
for i in range(0,square_size):
    if(sum(square_2d_array[i][j] for j in range(square_size)) != main_diagonal_size):
        list.append(i + 1) #because we are starting from 0

for j in range(0,square_size):
    if(sum(square_2d_array[i][j] for i in range(square_size)) != main_diagonal_size):
        list.append(-(j+1))
print(len(list))
# print(list)
list = sorted(list)
for i in range(0,len(list)):
    print(list[i])


