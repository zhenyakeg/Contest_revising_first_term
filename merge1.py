__author__ = 'student'
A = list(map(int,input().split()))
B = list(map(int,input().split()))
def merge(A,B):
    merged = [None for k in range(len(A)+len(B))]
    i, j, k = 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged[k] = A[i]
            i += 1
        else:
            merged[k] = B[j]
            j += 1
        k += 1
    merged[k:] = A[i:] + B[j:]
    return merged
print(*merge(A, B))