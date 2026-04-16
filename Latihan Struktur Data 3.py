barang = []
harga = []
total = 0

jumlah = int(input("masukkan jumlah barang: "))

for i in range(jumlah):
    nama = input(f"masukkan nama barang ke-{i+1}: ")
    h = int(input(f"masukkan harga {nama}: "))
     
    barang.append(nama)
    harga.append(h)
     
print("\nDaftar belanja:")
for i in range(len(barang)):
    print(f"{barang[i]} - Rp{harga[i]}")
    total += harga[i]
    
print("total bayar: Rp", total)



data = {}
total = 0

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    nama = input(f"Nama mahasiswa ke-{i+1}: ")
    nilai = int(input(f"Nilai {nama}: "))
    
    data[nama] = nilai
    total += nilai
    
rata = total / jumlah

print("\nData Mahasiswa:")
for nama, nilai in data.items():
    status = "Lulus" if nilai >= 75 else "Tidak Lulus"
    print(f"{nama} - Nilai: {nilai} - Status: {status}")
    
print("Rata-rata nilai:, rata")



users = {
     "admin": "1234",
     "user": "abcd"
 }

percobaan = 0
while percobaan < 3:
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        print("Login berhasil!")
        break
    else:
        print("Login gagal!")
        percobaan += 1
        
    if percobaan == 3:
        print("Akun diblokir!")
        
        
        
antrian = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah Antrian")
    print("2. Layani Nasabah")
    print("3. Lihat Antrian")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nama = input("Nama nasabah: ")
        antrian.append(nama)
        print(nama,  "masuk antrian")
         
    elif pilihan == "2":
        if len(antrian) > 0:
            print("Melayani:", antrian.pop(0))
        else:
            print("Antrian kosong")
            
    elif pilihan == "3":
        print("Antrian sekarang:", antrian)
        
    elif pilihan == "4":
        print("Terima kasih")
        break
    
    else:
        print("Pilihan tidak valid")
         
         
         
         
inventaris = {}
while True:
    print("\n=== MENU INVENTARIS ===")
    print("1. Tambah Barang")
    print("2. Kurangi Stok")
    print("3. Lihat Barang")
    print("4. Keluar")
     
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        nama = input("Nama barang: ")
        stok = int(input("Jumlah stok: "))
        inventaris[nama] = stok
        print("Barang ditambahkan")
        
    elif pilih == "2":
        nama = input("Nama barang: ")
        if nama in inventaris:
            jumlah = int(input("Jumlah yang diambil: "))
            if inventaris[nama] >= jumlah:
                inventaris[nama] -= jumlah
                print("Stok berhasil dikurangi")
            else:
                print("Stok tidak cukup")
        else:
            print("Barang tidak ditemukan")
            
    elif pilih == "3":
        print("\nDaftar Inventaris:")
        for barang, stok in inventaris.items():
            print(barang, "-", stok)
            
    elif pilih == "4":
        print("Program selesai")
        break
    
    else:
        print("Pilihan salah")