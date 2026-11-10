# 1.TUPLE
# a.Buat sebuah Tuple bernama mahasiswa 
mahasiswa = ("Windi Elika Sari", "2605060056", "Teknologi Informasi")

# b. Tampilkan data NIM dan prodi ke layar dengan mengakses indeksnya
# NIM berada di indeks 1, prodi berada di indeks 2
print("NIM:", mahasiswa[1])
print("prodi:", mahasiswa[2])

# c.Menampilkan mengubah nilai indeks ke-2 (Akan menghasilkan error)
mahasiswa[2] = "Teknologi Informasi"

# d. Buat sebuah set bernama nilai_angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("\nIsi nilai_angka:", nilai_angka)
# Penjelasan angka 10 dan 4: karakteristik utama dari set adalah duplikasi tidak diizinkan
# (unique elements). Angka 10 dan 4 yang ditulis dua kali secara otomatis dilebur menjadi satu.

# 2.Manipulasi Dictionary
# a. Buat dictionary data_mahasiswa
data_mahasiswa = {
    "nim": "2605060056",
    "nama": "Windi Elika Sari",
    "prodi": "Teknologi Informasi"
}

# b. Ubah nilai "Prodi" menjadi "Sastra Mesin" sekaligus menambahkan key baaru "angkatan" dengan nilai 2026.
data_mahasiswa["prodi"] = "sastra mesin"
data_mahasiswa["angkatan"] = 2026
del data_mahasiswa["nim"]
print("Hasil akhir dictionary")
print(data_mahasiswa)

# 3.Perulangan pada Dictionary
# a. Buat dictionary bernama keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Gunakan perulangan untuk menampilkan setiap barang dan harganya 
print("daftar Belanjaan:")
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")

#c. Tampilkan total belanja
total_belanja = sum(keranjang.values())
print(f"\nTotal belanja: Rp {total_belanja}")
