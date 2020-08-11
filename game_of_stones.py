test_cases = int(input())
result_list = []
for i in range(test_cases):
    number_of_games = int(input())
    pile_size_list = []
    sum = 0
    for j in range(number_of_games):
        piles = int(input())
        pile_sizes = input().split(" ")
        for t in pile_sizes:
            pile_size_list.append(int(t))
    for r in pile_size_list:
        sum += r//2
    if(sum % 2 == 0):
        result_list.append('Bob')
    else:
        result_list.append('Alice')

for result in result_list:
    print(result)


