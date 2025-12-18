s = input("Nhập chuỗi: ")

chu = so = dac_biet = 0

for c in s:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        chu += 1
    elif '0' <= c <= '9':
        so += 1
    else:
        dac_biet += 1

print("Chữ cái:", chu)
print("Chữ số:", so)
print("Ký tự đặc biệt:", dac_biet)