with open("vanban.txt", "r", encoding="utf-8") as f:
    content = f.read()

words = content.lower().split()
tan_suat = {}

for word in words:
    word = word.strip(",.")
    tan_suat[word] = tan_suat.get(word, 0) + 1

print("Danh sách từ và số lần xuất hiện:")
for word, count in tan_suat.items():
    print(f"{word}: {count}")