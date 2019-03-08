A = [4.06, 7, 5]  #вектори довільної (однакової)довжини
B = [1, -7, 0]
n = len(A)
d = 0
for i in range(n):
    d += (A[i] - B[i]) ** 2
d = d ** 0.5
d2 = round(d, 2) 
print('dist AB = ', d2)