max_len = 510
modulo = 1000000007
memorization = [[[0 for k in range(max_len)] for j in range(int(max_len / 2))] for i in range(int(max_len / 2))]
def Npalindroms(str,N):
    len1 = len(str)
    pair = int((len1+1)/2)
    no_mismatch = 0
    for i in range(pair):
        if(str[i] != str[len1-i-1]):
            no_mismatch += 1
    memorization[0][0][0] = 1
    for j in range(N+1):
        for k in range(1,pair+1,1):
            if (str[k - 1] != str[len1 - k]):
                flag1 = True
            else:
                flag1 = False
            if (not k-1 == len1 - k):
                flag2 = False
            else:
                flag2 = True
            for b in range(no_mismatch+1):
                if(flag2):
                    memorization[j][k][b] = memorization[j][k-1][b]
                    if(j > 0):
                        memorization[j][k][b] = (25 * memorization[j-1][k-1][b] + memorization[j][k][b]) % modulo
                else:
                    if(not flag1):
                        memorization[j][k][b] = (memorization[j][k-1][b])
                        if(j > 1):
                            memorization[j][k][b] = (memorization[j][k][b] + 25*memorization[j-2][k-1][b]) % modulo
                    if(flag1):
                        if(b > 0 and j > 0):
                            memorization[j][k][b] = 2 * memorization[j-1][k-1][b-1]
                        if(j>1):
                            memorization[j][k][b] = (memorization[j][k][b] + 24 * memorization[j-2][k-1][b-1]) % modulo
    return memorization[N][pair][no_mismatch]
test_cases = int(input())
for i in range(test_cases):
    input_list = input().split(" ")
    N = int(input_list[0])
    string = input_list[1]
    print(Npalindroms(string,N))



