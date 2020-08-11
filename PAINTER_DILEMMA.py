test_cases = int(input())
result_list = []
def what_brush_to_paint(colors,brush1_color,brush2_color,start):
    for i in range(start,len(colors)):
        if(brush1_color == int(colors[i])):
            return 2
        if(brush2_color == int(colors[i])):
            return 1
    return 1
for i in range(0,test_cases):
    changes = 1
    N = int(input())
    colors = input().split(" ")
    brush_2_current_color = 0
    brush_1_current_color = int(colors[0])
    for j in range(1,len(colors)):
        if(brush_1_current_color != int(colors[j])) and (brush_2_current_color != int(colors[j])):
            brush_to_change = what_brush_to_paint(colors,brush_1_current_color,brush_2_current_color,j+1)
            changes += 1
            if(brush_to_change == 1):
                brush_1_current_color = int(colors[j])
            else:
                brush_2_current_color = int(colors[j])
        else:
            continue
    result_list.append(changes)
for l in result_list:
    print(l)

