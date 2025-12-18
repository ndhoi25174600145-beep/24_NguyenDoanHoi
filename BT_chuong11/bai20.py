d = eval(input("Nhập dictionary: "))
kq = {}

for k in d:
    if d[k] > 50:
        kq[k] = d[k]

print(kq)
