def MatrixChainOrder(matrixChain):
    n = len(matrixChain)
    costMatrix = [[0 for i in range(n)] for i in range(n)]
    sol = [[0 for i in range(n)] for i in range(n)]

    for chainLength in range(2, n):
        for a in range(1, n - chainLength + 1):
            b = a + chainLength - 1

            costMatrix[a][b] = float('inf')
            for c in range(a,b):
                cost = costMatrix[a][c] + costMatrix[c+1][b] + matrixChain[a-1] * matrixChain[c] * matrixChain[b]
                if cost < costMatrix[a][b]:
                    sol[a][b] = c
                    costMatrix[a][b] = cost
    return costMatrix, sol

def printOptiomalSol(optimalSol, i, j):
    if i == j :
        print('A' + str(i), end='')
    else:
        print('(', end='')
        printOptiomalSol(optimalSol, i, optimalSol[i][j])
        printOptiomalSol(optimalSol, optimalSol[i][j]+1, j)
        print(')',end='')


def main():
    array=[30,35,15,5,10,20,25]
    n = len(array)
    costMatrix, optimalSol = MatrixChainOrder(array)
    printOptiomalSol(optimalSol, 1, n-1)
    print('\n' , costMatrix[1][len(array)-1])

if __name__ == '__main__':
    main()
