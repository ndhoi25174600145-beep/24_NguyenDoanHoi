def kiem_tra_so_doi_xung(n):
    s = str(n)          
    return s == s[::-1] 

n = int(input("Nhập số nguyên n: "))

if kiem_tra_so_doi_xung(n):
    print(n, "là số đối xứng")
else:
    print(n, "không phải số đối xứng")
