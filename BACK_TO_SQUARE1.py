N = int(input())
value = 1.0
while (N != 0):
    input_list = input().split(" ")
    for i in range(N - 1):
        value = ((value) * (1.0 / float(input_list[i])) + 1.0)
    print(int(round(value)))
    value = 1.0
    N = int(input())


