with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID,Ten san pham,Gia\n")
    f.write("1,Laptop,1200\n")
    f.write("2,Chuot may tinh,25\n")
    f.write("3,Ban phim,75\n")


id_can_sua = input("Nhập ID sản phẩm cần cập nhật: ")
gia_moi = input("Nhập giá mới: ")


with open("san_pham.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith(id_can_sua + ","):
        parts = line.strip().split(",")
        parts[2] = gia_moi
        line = ",".join(parts) + "\n"
    new_lines.append(line)


with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Cập nhật giá thành công!")