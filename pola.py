
print("Yazid-Dev")

print("================")
print("POLA:")
print("================")

print(f"""
1). Segitiga kiri atas
2). Segitiga kiri bawah
3). Segitiga kanan atas
4). Segitiga kanan bawah
5). Segitiga sama kaki kiri
6). Segitiga sama kaki kanan
7). Segitiga atas
8). Segitiga bawah
9). Belah ketupat

""")
print("================")
pil = int(input("PILIH POLA:")) 




if pil == 1 :

    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar = 0
    while bar < max_bar:
        kol = 0
        while kol < max_kol:
            print("*" if kol <= bar else " ", end=" ")
            kol+=1
        print("")
        bar+=1

elif pil == 2 :

    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar = 0
    while bar < max_bar:
        kol = max_kol
        while kol > 0 :
            print("*" if kol > bar else " ", end=" ")
            kol -= 1
        print("")
        bar += 1

elif pil == 3 :
    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar = 0

    while bar < max_bar:
        kol = max_kol
        while kol >= 0 :
            print("*" if kol <= bar else " ", end=" ")
            kol -=1
        print("")
        bar += 1

elif pil == 4 :

    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar = 0
    while bar < max_bar:
        kol = 0
        while kol < max_kol:
            print("*" if kol >= bar else " ", end=" ")
            kol += 1
        print("")
        bar += 1

elif pil == 5 :
    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar1 = 0

    while bar1 < max_bar:
        kol = max_kol
        while kol >= 0 :
            print("*" if kol <= bar1 else " ", end=" ")
            kol -=1
        print("")
        bar1 += 1

    bar2 = 1

    while bar2 < max_bar:
        kol = 0
        while kol <= max_kol:
            print("*" if kol > bar2 else " ", end=" ")
            kol += 1
        print("")
        bar2 += 1

elif pil == 6 :

    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar1 = 0
    while bar1 < max_bar:
        kol = 0
        while kol < max_kol:
            print("*" if kol <= bar1 else " ", end=" ")
            kol+=1
        print("")
        bar1+=1
    
    bar2 = 1
    while bar2 < max_bar:
        kol = max_kol
        while kol > 0 :
            print("*" if kol > bar2 else " ", end=" ")
            kol -= 1
        print("")
        bar2 += 1

elif pil == 7 :
    
    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar = 0

    while bar < max_bar:
        kol = max_kol
        while kol >= 0 :
            print("*" if kol <= bar else " ", end=" ")
            kol -=1
        kol = 1
        while kol < max_kol:
            print("*" if kol <= bar else " ", end=" ")
            kol+=1
        print("")
        bar += 1

elif pil == 8 : 

    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))

    bar = 0

    while bar < max_bar :
        kol = 0
        while kol < max_kol :
            print("*" if kol >= bar else " ", end=" ")
            kol+=1
        kol = max_kol - 1
        while kol > 0 :
            print("*" if kol > bar else " ", end=" ")
            kol -= 1
        print("")
        bar += 1

elif pil == 9 :

    max_bar = int(input("Masukkan maksimal baris:"))
    max_kol = int(input("Masukkan maksimal kolom:"))


    bar1 = 0

    while bar1 < max_bar:
        kol = max_kol
        while kol >= 0 :
            print("*" if kol <= bar1 else " ", end=" ")
            kol -=1
        kol = 1
        while kol < max_kol:
            print("*" if kol <= bar1 else " ", end=" ")
            kol+=1
        print("")
        bar1 += 1

    bar2 = 1

    while bar2 < max_bar :
        kol = 0
        while kol < max_kol :
            print("*" if kol > bar2 else " ", end=" ")
            kol+=1
        kol = max_kol - 1
        while kol >= 0 :
            print("*" if kol >= bar2 else " ", end=" ")
            kol -= 1
        print("")
        bar2 += 1

    





      


    
