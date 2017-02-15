__author__ = 'student'
s, m = tuple(map(int, input().split()))
A = list(map(int,input().split()))
check = [0 for i in range(len(A))]
''' число подмножеств сумма элементов меньше с произведение меньше м'''