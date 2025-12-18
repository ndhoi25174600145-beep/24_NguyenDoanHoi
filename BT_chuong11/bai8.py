a = list(map(int, input("Nhập danh sách: ").split()))
k = int(input("Nhập k: "))
n = len(a)

k = k % n
b = a[n-k:] + a[:n-k]
print(b)
