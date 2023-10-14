jumlah_buku = 10
total_jumlah_baca = 0
jumlah_buku_dibaca_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dibaca_dipahami}')
while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_dibaca_dipahami == 9:
        print(f'Buku ke {jumlah_buku_dibaca_dipahami + 1} belum paham')
    else:
        jumlah_buku_dibaca_dipahami = jumlah_buku_dibaca_dipahami + 1
        print(f'Buku ke {jumlah_buku_dibaca_dipahami} sudah dibaca dan dipahami')
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dibaca_dipahami}')
if jumlah_buku_dibaca_dipahami == jumlah_buku:
    print('Buku sudah dipahami semua')
else: print(f'Tidak semua buku bisa dipahami, hanya {jumlah_buku_dibaca_dipahami} saja yang paham')
