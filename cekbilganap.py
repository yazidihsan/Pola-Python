

a = int(input("batas awal: "))
b = int(input("batas akhir: "))

x = []
y = []

jumlah_angka = 0
for nilai in range(a, b+1):

    # print(b.count(nilai))
    if nilai % 2 == 0:
        x.append(nilai)
    else:
        y.append(nilai)
    if len(x) >= 5 and len(y) >= 5:
        break
    # if jumlah_angka == 5:
    #     break

print("nilai x :", x)
print("nilai y :", y)
