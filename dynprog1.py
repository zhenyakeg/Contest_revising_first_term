__author__ = 'student'
n = int(input())
F, G = [None], [None]
for i in range (1,n+1):
    if i <= 2:
        G.append(0)
        F.append(0)
    else:
        G.append(F[i - 2] + 2 * G[i - 1] - 1)
        F.append(F[i - 1] + 2 * G[i - 2] + 1)
print(F[n])
