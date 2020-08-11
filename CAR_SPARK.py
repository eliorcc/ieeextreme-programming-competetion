class Customer_0ffer:
    def __init__(self, start_time, end_time, money):
        self.start_time = start_time
        self.end_time = end_time
        self.money = money
def sortByEndTime(e):
    return e.end_time
def return_last_good_match_array(offers):
  p = [0] * len(offers)
  for i in range(1,len(offers)):
    for j in range(i,0,-1):
      if(offers[i].start_time >= offers[j-1].end_time):
        p[i] = j
        break
  return p
result_list = []

test_cases = int(input())
for i in range(0, test_cases):
    offers_list = []
    N = int(input())
    for j in range(0, N):
        single_offer_input = input()
        splitted = single_offer_input.split(" ")
        offers_list.append(Customer_0ffer((int(splitted[0])), int(splitted[1]), int(splitted[2])))
    offers_list.sort(key=sortByEndTime)
    p = return_last_good_match_array(offers_list)
    memorization_array = [0] * (N+1)
    for b in range(1,N+1):
      memorization_array[b] = max(memorization_array[b-1],memorization_array[p[b-1]] + offers_list[b-1].money)
    result_list.append(memorization_array[N])
for l in result_list:
  print(l)

