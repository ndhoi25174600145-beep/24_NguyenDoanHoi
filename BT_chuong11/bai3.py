s = input("Nhập chuỗi: ")
kq = ""
space = False

for c in s:
    if c == " ":
        if not space:
            kq += c
        space = True
    else:
        kq += c
        space = False

print(kq.strip())