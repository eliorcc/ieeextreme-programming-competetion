from queue import Queue
import math
def in_queue(q,num):
    queue_list = list(q.queue)
    for i in queue_list:
        if(int(i) == num):
            return True
    return False
def in_list(l,num):
    for i in l:
        if(int(i) == num):
            return True
    return False
result_list = []
num_of_test_cases = int(input())
for i in range(0,num_of_test_cases):
    test_case_variables = input()
    spitted_list_variables = (test_case_variables.split(" "))
    p = int(spitted_list_variables[0]) # number of pages the os allocates for the app
    s = int(spitted_list_variables[1]) # page size
    n = int(spitted_list_variables[2]) # number of accessed pages by the app
    queue = Queue(maxsize=p)
    page_replacements_for_fifo = 0
    append_list = []
    for j in range(0,n):
        to_insert = math.floor(int(input()) / s)
        append_list.append(to_insert)
        if((not queue.full()) and (not in_queue(queue,to_insert))):
            queue.put(to_insert)
        if((queue.full()) and (not in_queue(queue,to_insert))):
            queue.get()
            page_replacements_for_fifo = page_replacements_for_fifo + 1
            queue.put(to_insert)
        if((not queue.full()) and (not in_queue(queue,to_insert))):
            queue.put(to_insert)
        else:
            continue
    #now we have number of replacements for fifo algorithm
    #lets calcuate the number of replacements for lru algorithm
    lru_list = []
    page_replacements_for_lru = 0
    for j in range(0,n):
        if((len(lru_list) < p) and (not in_list(lru_list,append_list[j]))):
            lru_list.append(append_list[j])
        if((len(lru_list) == p) and (not in_list(lru_list,append_list[j]))):
            lru_list.pop(0)
            page_replacements_for_lru = page_replacements_for_lru + 1
            lru_list.append(append_list[j])
        if((in_list(lru_list,append_list[j]))):
            index = lru_list.index(append_list[j])
            lru_list.pop(index)
            lru_list.append(append_list[j])

    #now we have number of replacements for lru algorithm
    if(page_replacements_for_lru < page_replacements_for_fifo):
        result_list.append('yes {0} {1}'.format(page_replacements_for_fifo,page_replacements_for_lru))
    else:
        result_list.append('no {0} {1}'.format(page_replacements_for_fifo,page_replacements_for_lru))


# print(page_replacements_for_fifo,page_replacements_for_lru)
for i in result_list:
    print(i)












