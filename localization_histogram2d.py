def normalize_answer(answer):
    sum = 0
    range1 = range(len(answer))
    for i in range1:
        sum += sum(answer[i])
    q = []
    for i in range1:
        w = []
        for j in range(len(answer[i])):
            w.append(answer[i][j] / sum)
        q.append(w)
    return q
def sense(p, colors, measurement, sensor_right):
    q = []
    sensor_wrong = 1.0 - sensor_right
    len_colors = len(colors)
    for i in len_colors:
        w = []
        len_colors_i = len(colors[i])
        for j in len_colors_i:
            hit = (measurement == colors[i][j]) #bool
            current = p[i][j] * (hit * sensor_right + (1.0 - hit) * sensor_wrong) #הסתברות שלמה
            w.append(current)
        q.append(w)
    return normalize_answer(q)
def move(p, motion, p_move):
    q = []
    p_stay = 1.0 - p_move
    for i in range(len(p)):
        w = []
        for j in range(len(p[i])):
            s = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]) + \
                (p_stay * p[i][j])
            w.append(s)
        q.append(w)
    return q
def histogram_2d(colors, measurements, motions, sensor_right, p_move):
    pinitialize = 1.0 / float(len(colors)) / float(len(colors[0]))
    x = len(colors[0])
    y = len(colors)
    p = [[pinitialize for row in range(x)] for column in range(y)]
    #initialize all values
    len_measurments = len(measurements)
    for i in range(len_measurments):
        p = move(p, motions[i], p_move)
        p = sense(p, colors, measurements[i], sensor_right)
    return p
def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')
