# Program Kelulusan Ujian Mahasiswa

print("===== PROGRAM KELULUSAN UJIAN =====")

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa (Andi/Budi/Citra): ")

# Menentukan target nilai
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    target = 0
    print("Nama mahasiswa tidak terdaftar!")

# Proses ujian
if target != 0:
    print("Nama mahasiswa:", nama)
    print("Target nilai:", target)

    percobaan = 1
    nilai = 0

    while percobaan <= 3 and nilai < target:

        print("\nPercobaan ke-", percobaan)
        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            print("Selamat, kamu berhasil mencapai target!")
        else:
            print("Nilai belum mencapai target.")

        percobaan += 1

    # Hasil akhir
    if nilai >= target:
        print("\n", nama, "berhasil lulus!")
        print("Jumlah percobaan:", percobaan - 1)
    else:
        print("\n", nama, "dinyatakan tidak lulus.")
        print("Sudah melakukan 3 kali percobaan.")

        