listNama = ["Nadhira","Mama","Papa"]

namaDIcari = input("masukkan nama yang dicari: ")

for i, nama in enumerate(listNama):
    if nama.lower() == namaDIcari.lower():
        print(f"nama yang anda cari ada di index ke-{i}")
        break
else:
    print('Maaf, pencarian yang anda lakukan tidak ada di dalam list')