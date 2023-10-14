"""
Tolong beli susu 1, kalau ada telor beli 6
di case ini sebagai programmer, beli susu 1, jika ada telor, beli 6 susu
"""

jumlah_telor = 1
jumlah_susu = 23

print(f'Jumlah telur adalah {jumlah_telor} butir')
print(f'Jumlah susu adalah {jumlah_susu} botol')

if jumlah_susu > 0:
    print('Susu ada, dan uangnya cukup')
    if jumlah_telor == 0:
        print('Budi membeli 1 botol susu')
    else: print ('Budi membeli 6 botol susu')

