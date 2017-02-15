__author__ = 'student'
Q = []
for s in range (8):
    Q.append(tuple(map(int,input().split())))
def check(Q):
    for i in range (8):
        for j in range (i):
            if Q[j][0] == Q[i][0] or Q[j][1] ==  Q[i][1] or (Q[j][0]-Q[i][0])**2 == (Q[j][1]-Q[i][1])**2:
                return 'YES'
    return 'NO'
print(check(Q))
