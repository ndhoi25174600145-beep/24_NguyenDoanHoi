d = eval(input("Nhập dictionary: "))
new = {}

for k in d:
    new[d[k]] = k

print(new)