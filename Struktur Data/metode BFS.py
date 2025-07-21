# menyimpan daerah asal
graph1 = { 
 'depok': ['bekasi', 'jakarta', 'tanggerang', 'bogor'],
 'jakarta': ['depok', 'tanggerang', 'bekasi'],
 'tanggerang': ['depok', 'jakarta'],
 'bekasi': ['depok', 'bogor', 'jakarta'],
 'bogor': ['jakarta', 'bekasi', 'depok']
}
# menyimpan daerah tujuan
graph2 = {
    'depok' : ['ubsi margonda'],
    'jakarta' : ['ubsi keramat'],
    'tanggerang' : ['ubsi cimone'],
    'bekasi' : ['ubsi kalimalang'],
    'bogor' : ['ubsi cilebut'], 
}
print()
# inputan titik awal dan tujuan
awal = input('Masukkan titik awal   : ').lower()
tujuan = input('Masukkan titik tujuan : ').lower()
# invalid input
if awal not in graph1 or tujuan not in graph2:
    print()
    print("======= {Titik awal atau Titik tujuan tidak valid, rute tidak ditemukan.} =======")
    print()
  
# valid input    
else:
    rute_tercepat = []
    rute_terlama = []
    jalur = [[awal]]
    jumlah_tercepat = float('inf')
    jumlah_terlama = 0
    semua_jalur = []

    while jalur:
        jalur_aktif = jalur.pop(0)
        kota_terakhir = jalur_aktif[-1]

        if kota_terakhir == tujuan:          #Mencari semua kemunginan jalur yg dilewati dan menyimpan jalur yg berakhir dikota tujuan dan meyimpannya di variabel semua_jalur
            jumlah_kota = len(jalur_aktif)
            semua_jalur.append(jalur_aktif)
            if jumlah_kota < jumlah_tercepat: #Mencari rute tercepat dengan membandingkan jumlah kota yang dilewati 
                jumlah_tercepat = jumlah_kota
                rute_tercepat = jalur_aktif
            if jumlah_kota > jumlah_terlama: #Mencari rute terlama dengan membandingkan jumlah atau panjang kota yang dilewati
                jumlah_terlama = jumlah_kota
                rute_terlama = jalur_aktif

        for kota_sekitar in graph1.get(kota_terakhir, []): #Mengecek apakah sudah semua jalur dilewati dengan melakukan looping mengambil value dari graph1(kota_terakhir)
            if kota_sekitar not in jalur_aktif:
                jalur.append(jalur_aktif + [kota_sekitar])# Jika belum dilewati, tambahkan atau masukan jalur baru dengan kota_sekitar
    print()
    print('================= {Rute Yang Dilewati Untuk Menuju Kampus} ===================')
    print(f'Titik Awal           : {awal}')
    print('Titik Tujuan(Kampus) :',graph2[tujuan])
    print("Total kemungkinan jalur yang bisa dilewati : " + str(len(semua_jalur)) + " jalur ")
    print("Jalur yang ditemukan :", semua_jalur)
    print("Rute tercepat :", " -> ".join(rute_tercepat) if rute_tercepat else "Tidak ada")
    print("Rute terlama  :", " -> ".join(rute_terlama) if rute_terlama else "Tidak ada")
    print('==============================================================================')
    print()