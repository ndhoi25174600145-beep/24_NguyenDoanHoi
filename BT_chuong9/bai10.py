def quy_tinh_so_fibonacci(n):
    if n < 0:
        return "n phải là số nguyên không âm"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f0, f1 = 0, 1
        for _ in range(2, n + 1):
            f_next = f0 + f1
            f0, f1 = f1, f_next
        return f1
n = int(input("Nhập n: "))
print(f"Số Fibonacci thứ {n} là:", quy_tinh_so_fibonacci(n))

                
    