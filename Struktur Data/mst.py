# Ubah aja Graphnya Disini
a = ["a", "b", "c", "d", "e"] # Dari simpul ini
b = ["b", "c", "d", "e", "a"] # Ke simpul ini
v = [7, 11, 8, 9, 3 ] # valuenya 
#-------------------------------------------------
# input dan tampungan
awal = str(input("Masukan simpul awal = ")).lower()
akhir = str(input("Masukan simpul akhir = ")).lower()
jalur = []
vJalur = []
hasil = []
# mencari semua jalur dari awal ke akhir
def cari_jalur(posisi, total, dilewati):
    if posisi == akhir:
        vJalur.append(total), jalur.append(dilewati)
        return
    for i in range(len(a)):
        if a[i] == posisi and b[i] not in dilewati:
            cari_jalur(b[i], total + [v[i]], dilewati + [b[i]])
        elif b[i] == posisi and a[i] not in dilewati:
            cari_jalur(a[i], total + [v[i]], dilewati + [a[i]])
# menjumlahkan seluruh value dari tiap jalur ditemukan
def jumHasil() :
     for i in range (len(vJalur)) :
         hasil.append(sum(vJalur[i]))
# eksekusi function
cari_jalur(awal, [], [awal])
jumHasil()
print(f"Hasil pencarian semua ruas = {jalur} \nHasil value pencarian semua ruas = {vJalur}\nSemua total bobot dari {awal} ke {akhir} = {hasil}")
print(f"Minimum Spanning Tree = {min(hasil)}\nCritical Path = {max(hasil)}" if len(hasil) > 0 else "Tidak ada jalur ditemukan.")