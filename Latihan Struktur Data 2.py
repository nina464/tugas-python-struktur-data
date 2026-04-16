barang = ["beras", "gula", "minyak"]
harga = [12000, 8000, 15000]

total = 0

print("Daftar belaja:")
for i in range(len(barang)):
    print(f"{barang[i]} - Rp{harga[i]}")
    total += harga[i]

print("Total yang harus dibayar: Rp", total)


nilai_mahasiswa = {
    "Andi": 80,
    "Budi": 75,
    "Citra": 90,
    "Dina": 85
}

total = 0

for nama in nilai_mahasiswa:
    print(nama, ":", nilai_mahasiswa[nama])
    total += nilai_mahasiswa[nama]

rata_rata = total / len(nilai_mahasiswa)
print("Rata-rata nilai:", rata_rata)


users = {
    "admin": "1234",
    "user1": "abcd",
    "user2": "pass"
}

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in users:
    if users[username] == password:
        print("Login berhasil")
    else:
        print("Password salah")
else:
    print("Username tidak ditemukan")
    
    
    
antrian = []

# tambah pasien
antrian.append("Pasien A")
antrian.append("Pasien B")
antrian.append("Pasien C")

print("Antrian awal:", antrian)

while len(antrian) > 0:
    pasien = antrian.pop(0)
    print("Melayani:", pasien)
    print("Sisa antrian:", antrian)
    
    
    
transaksi = []
transaksi.append("Beli pulsa")
transaksi.append("Bayar listrik")
transaksi.append("Top up e-wallet")

print("Riwayat transaksi:", transaksi)

# batalkan transaksi terakhir
dibatalkan = transaksi.pop()

print("Transaksi dibatalkan:", dibatalkan)
print("Sisa transaksi:", transaksi)



inventaris = {
    "Pensil": 10,
    "Buku": 3,
    "Penghapus": 2,
    "Pulpen": 7
}

print("Barang dengan stok rendah:")

for barang, stok in inventaris.items():
    if stok < 5:
        print(barang, "- stok:", stok)
        


kalimat = "saya makan nasi saya minum air"
kata_list = kalimat.split()

frekuensi = {}

for kata in kata_list:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1

print("Frekuensi kata:")
for kata, jumlah in frekuensi.items():
    print(kata, ":", jumlah)
    
    
    
nilai = {
     "Andi": 80,
     "Budi": 60,
     "Citra": 75,
     "Dina": 70
 }

lulus = []
tidak_lulus = []

for nama, n in nilai.items():
    if n >= 75:
        lulus.append(nama)
    else:
        tidak_lulus.append(nama)
        
print("Mahasiswa lulus:", lulus)
print("Mahasiswa tidak lulus:", tidak_lulus)
 
 
 
pelanggan1 = ["Andi", "Budi", "Citra"]
pelanggan2 = ["Budi", "Dina", "Eka"]

gabungan = pelanggan1 + pelanggan2

unik = list(set(gabungan))

print("Semua pelanggan:", gabungan)
print("Pelanggan unik:", unik)



produk = [
    {"nama": "Laptop", "harga": 7000000},
    {"nama": "Mouse", "harga": 150000},
    {"nama": "Keyboard", "harga": 300000},
    {"nama": "Monitor", "harga": 2000000}
]

# sorting
produk.sort(key=lambda x: x["harga"])
print("Produk setelah diurutkan:")
for item in produk:
    print(item["nama"], "-", item["harga"])
    
    
    
    
