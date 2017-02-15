__author__ = 'student'
N = int(input())
diploma = dict()
attach = dict()
for i in range(N):
    a=input().split()
    diploma[a[0]] = int(a[1])
for j in range(N):
    b = input().split()
    attach[b[0]] = int(b[1])
for p in diploma:
    print(diploma[p], attach[p])

