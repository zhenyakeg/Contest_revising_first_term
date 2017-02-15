__author__ = 'student'
N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
sum = 0
for i in range(N // 2):
    A[N-1-i] = 0
for i in range(N):
    sum += A[i]
print(sum)
