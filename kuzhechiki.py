__author__ = 'student'
n = int(input())
A = list(map(int, input().split()))
t = int(input())
def jump(A, t):
    for i in range(t):
        tmp = A[-1]
        s = len(A)
        for i in range(tmp):
            A[s-1-i] = A[s-2-i]
        A[s-tmp-1] = tmp
    return A
print(*jump(A, t))
