batas = int(input("masukkan batas akhir tahun:"))
awal = int(input("masukkan batas awal tahun:"))

listKabisat = []
listBukanKabisat = []

def cekkabisat(i):
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0:
                listKabisat.append(i)
            else:
                listBukanKabisat.append(i)
        else:
            listKabisat.append(i)
    else:
        listBukanKabisat.append(i)


for i in range(awal,batas):
    cekkabisat(i)
       


print("merupakan tahun kabisat: ",listKabisat)
print("bukan tahun kabisat: ",listBukanKabisat)

