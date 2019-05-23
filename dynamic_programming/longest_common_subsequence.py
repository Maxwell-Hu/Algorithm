def lcs(x, y):
    m = len(x)
    n = len(y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # 到这里已经得到最长的子序列的长度，下面从这个矩阵中就是得到最长子序列
    seq = ''
    i, j = len(x), len(y)
    while i !=0 and j != 0:
        if L[i][j] == L[i-1][j]:
            i -= 1
        elif L[i][j] == L[i][j-1]:
            j -= 1
        else:
            assert x[i-1] == y[j-1]
            seq = x[i-1] + seq
            i -= 1
            j -= 1
    
    return  L[m][n], seq

if __name__ == '__main__':
    x = 'AGGTAB'
    y = 'GXTXAYB'
    print(lcs(x,y))