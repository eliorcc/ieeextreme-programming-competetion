test_cases = int(input())
result_list = []
def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
for t in range(test_cases):
    string = input()
    len1 = len(string)
    p = [0] * (len1)
    computeLPSArray(string,len1,p)
    result_list.append(len1-p[len1-1])
for i in result_list:
    print(i)

