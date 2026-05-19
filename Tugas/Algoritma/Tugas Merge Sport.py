def urutkan_naik(data):
    if len(data) <= 1:
        return data
    tengah = len(data) // 2
    kiri = urutkan_naik(data[:tengah])
    kanan = urutkan_naik(data[tengah:])
    return gabung_naik(kiri, kanan)

def gabung_naik(kiri, kanan):
    tampung = []
    ptr_kiri = 0
    ptr_kanan = 0
    while ptr_kiri < len(kiri) and ptr_kanan < len(kanan):
        if kiri[ptr_kiri] <= kanan[ptr_kanan]:
            tampung.append(kiri[ptr_kiri])
            ptr_kiri += 1
        else:
            tampung.append(kanan[ptr_kanan])
            ptr_kanan += 1
    tampung.extend(kiri[ptr_kiri:])
    tampung.extend(kanan[ptr_kanan:])
    return tampung


def urutkan_turun(data):
    if len(data) <= 1:
        return data
    tengah = len(data) // 2
    kiri = urutkan_turun(data[:tengah])
    kanan = urutkan_turun(data[tengah:])
    return gabung_turun(kiri, kanan)

def gabung_turun(kiri, kanan):
    tampung = []
    ptr_kiri = 0
    ptr_kanan = 0
    while ptr_kiri < len(kiri) and ptr_kanan < len(kanan):
        if kiri[ptr_kiri] >= kanan[ptr_kanan]:
            tampung.append(kiri[ptr_kiri])
            ptr_kiri += 1
        else:
            tampung.append(kanan[ptr_kanan])
            ptr_kanan += 1
    tampung.extend(kiri[ptr_kiri:])
    tampung.extend(kanan[ptr_kanan:])
    return tampung


def urutkan_nama(data):
    if len(data) <= 1:
        return data
    tengah = len(data) // 2
    kiri = urutkan_nama(data[:tengah])
    kanan = urutkan_nama(data[tengah:])
    return gabung_nama(kiri, kanan)

def gabung_nama(kiri, kanan):
    tampung = []
    ptr_kiri = 0
    ptr_kanan = 0
    while ptr_kiri < len(kiri) and ptr_kanan < len(kanan):
        if kiri[ptr_kiri].lower() <= kanan[ptr_kanan].lower():
            tampung.append(kiri[ptr_kiri])
            ptr_kiri += 1
        else:
            tampung.append(kanan[ptr_kanan])
            ptr_kanan += 1
    tampung.extend(kiri[ptr_kiri:])
    tampung.extend(kanan[ptr_kanan:])
    return tampung


def tampilkan_menu():
    print("\n======== PROGRAM SORTING DATA ========")
    print("1. Urutkan Angka dari Kecil ke Besar")
    print("2. Urutkan Angka dari Besar ke Kecil")
    print("3. Urutkan Daftar Nama")
    print("4. Keluar Program")
    print("======================================")

def input_angka():
    n = int(input("Berapa banyak angka yang ingin diinput? "))
    daftar = []
    for urutan in range(1, n + 1):
        nilai = int(input(f"  Angka ke-{urutan}: "))
        daftar.append(nilai)
    return daftar

def input_nama():
    n = int(input("Berapa banyak nama yang ingin diinput? "))
    daftar = []
    for urutan in range(1, n + 1):
        nilai = input(f"  Nama ke-{urutan}: ")
        daftar.append(nilai)
    return daftar


while True:
    tampilkan_menu()
    pilih = input("Pilihan Anda: ").strip()

    if pilih == "1":
        daftar_angka = input_angka()
        hasil = urutkan_naik(daftar_angka)
        print("\nSebelum diurutkan :", daftar_angka)
        print("Setelah diurutkan  :", hasil)

    elif pilih == "2":
        daftar_angka = input_angka()
        hasil = urutkan_turun(daftar_angka)
        print("\nSebelum diurutkan :", daftar_angka)
        print("Setelah diurutkan  :", hasil)

    elif pilih == "3":
        daftar_nama = input_nama()
        hasil = urutkan_nama(daftar_nama)
        print("\nSebelum diurutkan :", daftar_nama)
        print("Setelah diurutkan  :", hasil)

    elif pilih == "4":
        print("\nTerima kasih, program dihentikan.")
        break

    else:
        print("\nPilihan tidak valid, coba lagi.")
