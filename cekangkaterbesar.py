a = int(input('masukkan angka ke-1:'))
b = int(input('masukkan angka ke-2:'))
c = int(input('masukkan angka ke-3:'))

if a > b and a > c:
    print(f"{a} merupakan bilangan terbesar dari 3 angka")
elif b > a and b > c:
    print(f"{b} merupakan bilangan terbesar dari 3 angka")
else:
    print(f"{c} merupakan bilangan terbesar dari 3 angka")
