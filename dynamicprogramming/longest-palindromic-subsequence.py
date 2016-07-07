# link site is http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/
def lps(str):
    n = len(str)

    L = [[0 for col in range(n)] for row in range(n)]

    for i in range(n):
        L[i][i] =1

    #count
    for cl in range(2, n+1):
         for i in range(0, n-cl+1):
            j= i+cl-1

            if str[i] == str[j] and cl ==2 :
                L[i][j] =2
            elif str[i] == str[j]:
                 L[i][j] = L[i+1][j-1] + 2
            else :
                L[i][j] = max(L[i][j-1], L[i+1][j])
    print(L)
    return L[0][n-1];

print(lps("ABACAA"))