def kiem_tra_so_armstrong(n):
    s = str(n)
    tong = 0
    for c in s:
        tong += int(c)**3
    return tong == n

n = int(input("Nhập số nguyên dương n: "))
if kiem_tra_so_armstrong(n):
    print(n, "là số Armstrong")
else:
    print(n, "không phải số Armstrong")