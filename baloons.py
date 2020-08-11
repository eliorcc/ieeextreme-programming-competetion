num_baloon = 10
num_color = 3
class Question:
    def __init__(self,type,count,index,color):
        self.type = type #1 = color 2 = count
        self.count = count
        self.index = index
        self.color = color
    def isTrue(self,colors):
        if(type == 1):
            truth = (colors[self.index] == colors)
        if(type == 2):
            c = 0
            for i in range(num_baloon):
                if(colors[i] == self.color):
                    c += 1
            truth = (c == self.count)
        return truth
class Questions:
    def __init__(self,combine,truth,questions):
        self.combine = 1 # 1 and 2 or
        self.truth = truth
        self.questions = questions
    def isTrue(self,colors):
        if(self.combine == 1):
            result = True
        if(self.combine == 2):
            result = False
        for i in range(len(self.questions)):
            if(self.combine == 1):
                result = result and self.questions[i].isTrue(self.colors)
                if(not result):
                    break
            if(self.combine == 2):
                result = result or self.questions[i].isTrue(self.colors)
                if(result):
                    break
        return result
    def satisfy(self,colors):
        return self.isTrue(colors) == self.truth

T = int(input())
for i in range(T):
    q_l_list = input().split(" ")
    Q = q_l_list[0]
    L = q_l_list[1]
    lines = []
    for q in range(Q):
        while(1):
            type = input()
            if(type == "color"):
                input_list = input().split(" ")
                index = input_list[0]
                color = input_list[1]
                question = Question(1,0,index-1,color[0])
            if(type == "count"):
                input_list = input().split(" ")
                color = input_list[0]
                count = input_list[1]
                question = Question(2,count,0,color[0])
            lines.append(question)
            answer = input()
            if(answer == "yes"):
                lines[q].tr









def number2colors(number,colors):
    for i in range(num_baloon):
        color = number % num_color
        number /= num_color
        if(color == 0):
            colors[i] = 'r'
        if(color == 1):
            colors[i] = 'g'
        if(color == 2):
            colors[i] = 'b'
