import math
def test1(points,UCL,LCL):
    for point in points:
        if(point > UCL or point < LCL):
            return False
    return True
def test2(points,SIGMA,CL):
    upper_min = CL + 2*SIGMA
    lower_max = CL - (2*SIGMA)
    for i in range(len(points) - 2):
        counter_lower = 0
        counter_upper = 0
        for j in range(3):
            if(points[i+j] > upper_min):
                counter_upper += 1
            if(points[i+j] < lower_max):
                counter_lower += 1
        if(counter_lower > 1 or counter_upper > 1):
            return False
    return True
def test3(points,SIGMA,CL):
    upper_min = CL + SIGMA
    lower_max = CL - SIGMA
    for i in range(len(points)-4):
        counter_lower = 0
        counter_upper = 0
        for j in range(5):
            if(points[i+j] > upper_min):
                counter_upper += 1
            if(points[i+j] < lower_max):
                counter_lower += 1
        if(counter_lower > 3 or counter_upper > 3):
            return False
    return True
def test4(points,CL):
    for i in range(0,len(points)-7):
        counter_lower = 0
        counter_upper = 0
        for j in range(8):
            if(points[i+j] > CL):
                counter_upper += 1
            if(points[i+j] < CL):
                counter_lower += 1
        if(counter_upper == 8 or counter_lower == 8):
            return False
    return True
A2_ARRAY = [1.880,1.023,0.729,0.577,0.483,0.419,0.373,0.337,0.308]
test_cases = int(input())
for i in range(test_cases):
    input_list = input().split(" ")
    len_input = len(input_list)
    for li in range(len_input):
        input_list[li] = int(input_list[li])
    n = input_list[0]
    groups = input_list[1]
    average = 0
    range_average = 0
    for j in range(2,len_input,groups):
        max_subgroup = max(input_list[j:j+groups])
        min_subgroup = min(input_list[j:j+groups])
        group_range = abs(max_subgroup-min_subgroup)
        range_average = range_average + group_range
        average = average + sum(input_list[j:j+groups])

    range_average = range_average/math.ceil((len_input-2)/groups)
    average = average/(len(input_list)-2)
    UCL = average + A2_ARRAY[groups-2]*range_average
    LCL = average - A2_ARRAY[groups-2]*range_average
    CL = average
    SIGMA = (UCL-CL)/3
    input_list = input_list[2:len_input-1]
    if(test1(input_list,UCL,LCL) == False) or (test2(input_list,SIGMA,CL) == False) or (test3(input_list,SIGMA,CL) == False) or (test4(input_list,CL) == False):
        print("Out of Control")
    else:
        print("In Control")









