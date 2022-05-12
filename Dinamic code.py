def fib(n):
    fib = [0,1] + [0] * (n-1)
    for i in range(2,n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[n]
n = 9
fib(n)
print(fib(n))

'''grasehopper task, chess king'''
def lcs(A,B):
    '''Поиск длины общей последовательности'''
    F = [[0] * (len(B)+1) for i in range(len(A)+1)]
    for i in range(1,len(A) + 1):
        for j in range(1,len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    return F[-1][-1]
def gis(A,B):
    '''Наибольшая возрастающая последовательность'''
    F = [0] * (len(A) + 1)
    for i in range(1,len(A) + 1):
        m = 0
        for j in range(0,i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]
A = [105,0,56,96,90]
B = [105,0,56,73,90]
print(lcs(A,B))
gis(A,B)
print(gis(A,B))
