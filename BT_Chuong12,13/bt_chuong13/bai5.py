source_file = "san_pham.txt"
dest_file = "san_pham_copy.txt"

with open(source_file, "rb") as src, open(dest_file, "wb") as dst:
    while True:
        chunk = src.read(1024)
        if not chunk:
            break
        dst.write(chunk)

print("Sao chép tập tin thành công!")
