nilai = int(input("Masukkan nilai anda : "))
usia = int(input("Masukkan usia anda : "))

if nilai >= 75 :
    if usia < 17 :
        print("Selamat dek, kamu lulus")
    else:
        print("Selamat kak, kamu lulus")
else:
    if usia < 17 :
        print("Maaf dek, kamu belum lulus")
    else:
        print("Maaf kak, kamu belum lulus")
