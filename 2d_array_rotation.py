__author__ = 'student'
n, m = tuple(map(int, input().split()))
A = []
for i in range ( n ):
    A.append(list(map(int, input().split())))
for i in range (m):
    print(*[A[n-j-1][i] for j in range(n)])

