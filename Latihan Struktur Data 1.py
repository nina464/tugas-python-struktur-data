
belanja =["beras","gula","minyak","telur"]

print("Daftar belanja:")
for barang in belanja:
    print("-",barang)
    

menu = ["nasi goreng","mie ayam","soto","gado-gado"]

menu.append("bakso")
menu.remove("soto")

print("menu terbaru:", menu)


nilai = [78, 85, 90, 67, 88]

nilai_tertinggi = max(nilai)

print("nilai mahasiswa:", nilai)
print("nilai_tertinggi:", nilai_tertinggi)



antrian = []

antrian.append("pelanggan 1")
antrian.append("pelanggan 2")
antrian.append("pelanggan 3")

print("Antrian awal:", antrian)

dilayani = antrian.pop(0)

print("Yang dilayani:", dilayani)
print("Sisa antrian:", antrian)



riwayat = []

riwayat.append("google.com")
riwayat.append("youtobe.com")
riwayat.append("github.com")

print("riwayat browser:", riwayat)

halaman_terakhir = riwayat.pop()

print("Kembali dari halaman:", halaman_terakhir)
print("Halaman sekarang:", riwayat[-1])



produk = {
    "nama": "laptop",
    "harga": 7500000,
    "stok": 12
}

print("Data produk:")
print("Nama:", produk["nama"])
print("Harga:", produk["harga"])
print("Stok:", produk["stok"])



produk = {
    "nama": "laptop",
    "nama": 7500000,
    "stok": 12
}

produk["stok"] -=2

print("Data produk setelah perjualan:")
print(produk)




siswa = ["Andi","Budi","Andi","Citra","Budi","Dina"]

siswa_unik = set(siswa)

print("Daftar siswa unik:", siswa_unik)




piket = ("Alya", "Bima", "Caca", "Dino",)

print("Petugas piket hari ini:")
for siswa in piket:
    print("-", siswa)
    
    


harga_barang = [15000, 500, 12000, 20000, 8000]

harga_barang.sort()

print("Harga dari tamurah ke termahal:", harga_barang)