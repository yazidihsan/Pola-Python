# max_baris = int(input("Masukkan nilai maksimal baris:"))
# max_kolom = int(input("Masukkan nilai maksimal kolom:"))

# baris = 0       

# while baris < max_baris:                                
#     kolom = 0
#     while kolom < max_kolom:
#         print('+' if kolom < baris else "0" ,end=' ')
#         kolom+=1
#     else:
#         print('')
#     baris+=1

import re

listKota = ["Jakarta","Surabaya","Bandung"]

listHurufVokal = ['a','i','u','e','o']

for kota in listKota:
    print('[' + kota + ']')
    for vokal in listHurufVokal:
        print('-->', re.sub('[aiueo]', vokal, kota))