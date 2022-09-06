
maksimal_baris = int(input("Masukkan batas baris:"))
maksimal_kolom = int(input("Masukkan batas kolom:"))

baris = 0

while baris < maksimal_baris:
    kolom = 0
    while kolom < maksimal_kolom:
        print("o" if kolom >= baris else "+", end=' ')
        kolom += 1
    print('')
    baris += 1
