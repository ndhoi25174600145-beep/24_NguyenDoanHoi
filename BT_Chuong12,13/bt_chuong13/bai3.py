numbers = [1, 3, 5, 7, 9, 11, 13]

with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for num in numbers:
        f.write(str(num) + "\n")

print("Đã ghi danh sách số nguyên vào file so_nguyen.txt")