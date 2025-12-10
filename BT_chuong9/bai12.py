kiem_tra_chan = lambda n: n % 2 == 0
n = int(input("Nhập số cần kiểm tra: "))

if kiem_tra_chan(n):
    print(n, "là số chẵn")
else:
    print(n, "là số lẻ")