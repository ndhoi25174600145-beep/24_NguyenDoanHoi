
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    return -b / a


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

ket_qua = giai_phuong_trinh_bac_nhat(a, b)
print("Kết quả:", ket_qua)


