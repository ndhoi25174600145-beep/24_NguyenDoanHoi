s = input("Nhập chuỗi: ")
d = {}

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(d)
