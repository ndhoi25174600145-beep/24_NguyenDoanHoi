def so_le_lon_nhat(a, b, c):
    danh_sach = [x for x in [a, b, c] if x % 2 != 0] 
    if len(danh_sach) == 0:
        return -1  
    return max(danh_sach)



a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
kq = so_le_lon_nhat(a, b, c)
print("Số lẻ lớn nhất là:", kq)
