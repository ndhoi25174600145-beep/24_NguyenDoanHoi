def tong_chu_so(n):
    tong = 0
    for c in str(n):
        tong += int(c)
    return tong

n = int(input("Nhập số nguyên dương n: "))
print("Tổng các chữ số của", n, "là:", tong_chu_so(n))
