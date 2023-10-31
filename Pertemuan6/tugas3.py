jumlahbaris = int(input("Masukkan jumlah baris: "))

for bntng in range(1, jumlahbaris + 1):
    for br in range(bntng):
        print("*", end="")
    print()
