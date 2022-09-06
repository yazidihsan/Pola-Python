# n = 1


# while n <= 100: 
    
#     if n > 1:
#         for i in range(2,n):
#             if n%i == 0:
#                 break
#         else:
#             print(n)
#     n+=1

listKota = ['Bandung','Makassar','Semarang','Palembang','Jakarta','Bogor',

'Surabaya','Yogyakarta']

kotaYangDicari = input("Kota yang dicari: ")

n = 0

while n < len(listKota):
    if listKota[n].lower() == kotaYangDicari.lower():
        print("kota ketemu di index ke",n)
        break

    print('Bukan',listKota[n])
    n+=1

else:
    print("Maaf kota yang anda cari tidak ditemukan.")
    