
list = []
x = input()
while(x != 'END'):
    list.append(x)
    x = input()
list_len = len(list)
#print(list,list_len)
for x in list:
    count = 1
    while x != str(len(x)):
        count += 1
        x = str(len(x))
    print(count)
