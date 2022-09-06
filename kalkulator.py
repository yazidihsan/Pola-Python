print(20*"=")

x = int(input('masukkan angka pertama:'))
y = int(input('masukkan angka kedua:'))

hasil = 0


def tambah(a, b):
    hasil = a + b
    print(f"{x} + {y} = {hasil}")
    return hasil


def kurang(a, b):
    hasil = a - b
    print(f"{x} - {y} = {hasil}")
    return hasil


def kali(a, b):
    hasil = a*b
    print(f"{x} x {y} = {hasil}")
    return hasil


def bagi(a, b):
    hasil = a/b
    print(f"{x} : {y} = {hasil}")
    return hasil


def mod(a, b):
    hasil = a % b
    print(f"{x} % {y} = {hasil}")
    return hasil


def cekganjilgenap(cek):
    if cek % 2 == 0:
        print(f"{cek} merupakan bilangan genap")
    else:
        print(f"{cek} merupakan bilangan ganjil")


print("""\n Pilih operasi:
      1. Tambah (+)
      2. Kurang (-)
      3. Kali   (x)
      4. Bagi   (:)
      5. Modulo (%)
      """)
operasi = eval(input("Pilih operasi (+,-,x,:,%) "))

if operasi not in [1, 2, 3, 4]:
    print("Maaf operasi matematika anda tidak valid")

if operasi == 1:
    cek = tambah(x, y)

    cekganjilgenap(cek)

elif operasi == 2:
    cek = kurang(x, y)
    cekganjilgenap(cek)

elif operasi == 3:
    cek = kali(x, y)
    cekganjilgenap(cek)

elif operasi == 4:
    cek = bagi(x, y)
    cekganjilgenap(cek)

elif operasi == 5:
    cek = mod(x, y)
    cekganjilgenap(cek)

print(20*"=")
