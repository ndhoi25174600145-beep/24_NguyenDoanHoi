d = eval(input("Nhập dictionary: "))
kq = {}

for ten in d:
    diem = d[ten]
    if diem not in kq:
        kq[diem] = [ten]
    else:
        kq[diem].append(ten)

print(kq)