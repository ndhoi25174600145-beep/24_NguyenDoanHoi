kiem_tra_duong = lambda n: n > 0

n = float(input("Nhập số cần kiểm tra: "))

if kiem_tra_duong(n):
    print(n, "là số dương")
else:
    print(n, "không phải số dương")