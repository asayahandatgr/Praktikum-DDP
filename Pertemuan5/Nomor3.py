Ket ='''Selamat datang di perhitungan rumus : 
        1. Untuk Menghitung Luas Persegi
        2. Untuk Menghitung Luas Lingkaran
        3. Untuk Menghitung Luas Segitiga'''
print(Ket)
pilihan = input("Pilihanmu?")

match pilihan:
    case  "1":
        print("Rumus Persegi adalah")
        sisi =int(input("Masukkan Panjang Sisi Persegi"))
        luasP= sisi*sisi
        print("Luas Persegi Adalah", luasP)
match pilihan:
    case  "2":
        print("Rumus Lingkaran adalah")
        jari2= float(input("Masukkan Jari Jari"))
        luasL= 3.14 * jari2 * jari2
        print("luas lingkaran yang jari2nya", luasL)
match pilihan:
    case  "3":
        print("Rumus Segitiga adalah")
        alas= int(input("Masukkan Nilai Alas"))
        tinggi=float(input("Masukkan Nilai Tinggi"))
        luasS= (0.5) * alas * tinggi
        print("Luas Segitiga adalah", luasS)
    case _:
        print("Pilihanmu Salah! Silahkan Coba Lagi")
