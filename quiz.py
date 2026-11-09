# Program Kelulusan Ujian Mahasiswa

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    exit()

print("Nama mahasiswa :", nama)
print("Target nilai   :", target)

# Perulangan ujian maksimal 3 kali
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"Masukkan nilai ujian ke-{percobaan}: "))

    if nilai >= target:
        lulus = True
        break
    else:
        print("Nilai belum mencapai target!")
        percobaan += 1

# Menampilkan hasil akhir
if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan!")

