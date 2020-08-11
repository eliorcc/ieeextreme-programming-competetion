
test_cases = int(input())
result_list = []
#a function that i wrote to calculate log(num) in base N
#i have not used math.log because i have got a timeout termination
def closest_power_of_2(num):
    count = 0
    while (num > 0):
        num //= 2
        count += 1
    return count
for j in range(0,test_cases):
    N = int(input())
    count = closest_power_of_2(N)
    #now lets calculate the index of this number after the power of 2
    index_after_power_of_2 = N - (2**(count-1)-1)
    #now we will calculate the answer
    #multiply by 2 because the jumps are in 2 (1,3,5..)
    result_list.append(2*index_after_power_of_2-1)
for i in range(0,len(result_list)):
    print(int(result_list[i]))



