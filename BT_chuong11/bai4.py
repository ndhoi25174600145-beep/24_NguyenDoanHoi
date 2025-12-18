a = list(map(int, input("Nhập danh sách: ").split()))

max1 = max2 = -10**9
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and x > max2:
        max2 = x

print("Giá trị lớn thứ hai:", max2)
