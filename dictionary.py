# pertemuan_hari_ini = {
#     "judul" : "Belajar Dictionary Pada Python3",
#     "tanggal" : "28 Juli 1993",
#     "kategori": [
#         "Python Dasar", "Python Intermediete"
#     ],
#     "page_views" : 10,
#     "published": True,
#     "share_count": {
#         "facebook" : 0,
#         "twitter" : 2
#     }
# }

# buku = {
#     "judul" : "Hafalan Sholat Lima Waktu",
#     "Penulis" : "Susanto"
# }

# for key in buku:
#     print(key, '->', buku[key])


# print('Judul:', pertemuan_hari_ini.get('judul'))
# #atau
# print('Tanggal:', pertemuan_hari_ini['tanggal'])

# #Bisa menggunakan fungsi berantai untuk dictionary bertingkat
# print('Facebook share:', pertemuan_hari_ini.get('share_count').get('facebook'))

# print('Twitter share:', pertemuan_hari_ini['share_count']['twitter'])

# share_count = pertemuan_hari_ini.get('share_count')

# # print('Instagram share: ',share_count['instagram'])

# print('Instagram share: ',share_count.get('instagram'))

# buku = {
#     "judul": "Menghitung Algoritma",
#     "penulis": "Tere liye"
# }

# for judul, nilai in buku.items():
#     print(judul, '->', nilai)

# mahasiswa = {
#     "nama" : "Anton",
#     "asal" : "Pekalongan"
# }

# print("Data awal: ", mahasiswa["nama"])
# mahasiswa["nama"] = "Sasuke"
# print("Data update: ", mahasiswa.get("nama"))

# mahasiswa = {
#     "nama" : "Yazid Ihsan",
#     "asal" : "Salatiga"
# }

# print("Hobi : ", mahasiswa.get("hobi"))

# mahasiswa["hobi"] = "Ngoding"

# print("Hobi dari {} adalah {}".format(
#     mahasiswa.get("nama"),
#     mahasiswa.get("hobi")
# ) )

# mahasiswa = {
#     "nama": "Wahid",
#     "usia" : 18,
#     "asal" : "Cirebon"
# }

# # del mahasiswa["nama"]
# del mahasiswa["usia"]
# # del mahasiswa["asal"]
# # mahasiswa.pop('usia')
# # mahasiswa.pop('asal')

# print(mahasiswa.get("usia"))


# pesan_singkat = {
#     "isi" : "ISI PESAN INI HANYA BISA DIBACA SEKALI SAJA!!"
# }

# isi_pesan = pesan_singkat.pop("isi")

# print('isi pesan : ', pesan_singkat.get('isi'))

# print('isi pesan: ', isi_pesan)

# siswa = {
#     "nama" : 'Renza Ilhami',
# }

# print('Apakah variabel siswa memiliki key nama?')
# print('nama' in siswa)

# print('\nApakah variabel siswa TIDAK memiliki usia?')
# print('usia' not in siswa)

sekolah = {
    'nama': 'Sekolah Dasar Negeri Surabaya 1',
    'jenjang' : 'Sekolah Dasar',
    'akreditasi' : 'A',
    'alumni' : 0
}

print(
    "Jumlah atribut sekolah adalah:",
    len(sekolah)
)