d = eval(input("Nhập dictionary: "))

max_key = None
max_val = -10**9

for k in d:
    if d[k] > max_val:
        max_val = d[k]
        max_key = k

print(max_key)