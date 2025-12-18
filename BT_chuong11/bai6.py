a = list(map(int, input("Nhập danh sách: ").split()))
chan = le = 0

for x in a:
    if x % 2 == 0:
        chan += x
    else:
        le += x

print("Tổng chẵn:", chan)
print("Tổng lẻ:", le)
