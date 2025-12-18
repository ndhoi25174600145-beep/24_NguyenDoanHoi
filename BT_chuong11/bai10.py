m = int(input("Số hàng: "))
n = int(input("Số cột: "))

a = []
for i in range(m):
    a.append(list(map(int, input().split())))

max_sum = -10**9
row = 0

for i in range(m):
    s = 0
    for x in a[i]:
        s += x
    if s > max_sum:
        max_sum = s
        row = i

print("Hàng:", row)
