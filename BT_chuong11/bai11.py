n = int(input("Nhập n: "))
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

dx = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            dx = False

print("Đối xứng" if dx else "Không đối xứng")
