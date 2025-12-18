t = tuple(map(int, input("Nhập tuple: ").split()))
chan = ()
le = ()

for x in t:
    if x % 2 == 0:
        chan += (x,)
    else:
        le += (x,)

print(chan, sum(chan))
print(le, sum(le))
