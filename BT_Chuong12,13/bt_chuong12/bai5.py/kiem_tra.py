import sys
sys.path.append("../thu_vien_chung")

from xu_ly_so import kiem_tra_so_nguyen_to

n = int(input("Nhập số: "))
print("Là số nguyên tố?", kiem_tra_so_nguyen_to(n))
