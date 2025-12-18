m = int(input("m: "))
n = int(input("n: "))
p = int(input("p: "))

A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(n)]

C = [[0]*p for _ in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)
