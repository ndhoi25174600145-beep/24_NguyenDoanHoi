tim_min = lambda lst: min(lst)
n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

print("Danh sách:", lst)
print("Số nhỏ nhất trong danh sách là:", tim_min(lst))
