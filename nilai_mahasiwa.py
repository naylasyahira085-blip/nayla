print("=== SISTEM PENILAIAN MAHASISWA ===")

# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa (5-10): "))

if jumlah >= 5 and jumlah <= 10:

    total = 0

    # Perulangan input nilai
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))

        total = total + nilai

        # Menentukan status mahasiswa
        if nilai >= 90:
            status = "Lulus"
        else:
            status = "Tidak Lulus / Remedial"

        print(f"Status mahasiswa {i}: {status}")

    # Menghitung rata-rata
    rata_rata = total / jumlah

    # Menampilkan hasil
    print("\n=== HASIL PENILAIAN ===")
    print("Jumlah mahasiswa:", jumlah)
    print("Total nilai:", total)
    print("Nilai rata-rata:", rata_rata)