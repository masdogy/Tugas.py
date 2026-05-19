def bagi_array(data):
    if len(data) <= 1:
        return data
    
    tengah = len(data) // 2
    bagian_kiri = data[:tengah]
    bagian_kanan = data[tengah:]
    
    kiri_terurut = bagi_array(bagian_kiri)
    kanan_terurut = bagi_array(bagian_kanan)
    
    return gabungkan(kiri_terurut, kanan_terurut)


def gabungkan(kiri, kanan):
    array_hasil = []
    i = 0
    j = 0
    
    while i < len(kiri) and j < len(kanan):
        if kiri[i] >= kanan[j]:
            array_hasil.append(kiri[i])
            i += 1
        else:
            array_hasil.append(kanan[j])
            j += 1
    
    sisa_kiri  = kiri[i:]
    sisa_kanan = kanan[j:]
    
    array_hasil.extend(sisa_kiri)
    array_hasil.extend(sisa_kanan)
    
    return array_hasil


angka = [64, 25, 12, 22, 11]
print("Data awal        :", angka)
print("Urutan menurun   :", bagi_array(angka))
