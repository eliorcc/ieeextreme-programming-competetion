
def difference_calculator(sorted_dogs_size_list):
    difference_list = []
    l = len(sorted_dogs_size_list)
    for i in range(0,l):
        difference_list.append(sorted_dogs_size_list[l-1-i] - sorted_dogs_size_list[l-i-2])
    return sorted(difference_list)


test_cases = int(input())
result_list = []
for i in range(0, test_cases):
    list = (input().split(" "))
    dogs = int(list[0])
    dog_walkers = int(list[1])
    dogs_size_list = []
    for j in range(0, dogs):
        dogs_size_list.append(int(input()))
    dogs_size_list.sort()
    dif_list = difference_calculator(dogs_size_list)
    sum1 = 0
    for f in range(0,dog_walkers-1):
        sum1 = sum1 + dif_list.pop(len(dif_list)-1)
    one_group_answer = (dogs_size_list[dogs-1] - dogs_size_list[0])
    result_list.append(one_group_answer - sum1)
for t in result_list:
    print(t)
