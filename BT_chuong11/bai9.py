n = int(input("25: "))
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

tong = 0
for i in range(n):
    tong += a[i][n - i - 1]

print("Tổng:", tong)
