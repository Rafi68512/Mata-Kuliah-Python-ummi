"""
Pemrogram       : Muhammad Rafi
NIM             : 2130511003
Nama berkas     : Tugas_queue.py
Tujuan          : Membuat queue untuk menambah data, dan mencari data
Text Editor     : Visual Code Studio
Operating System: Windows 11
"""
from collections import deque

print('Nama : Muhammad Rafi')
print('Nim  : 2130511003\n')

print('=' * 70, '\n')

def cari(antrian, cari_angka):
    for i in range(len(antrian)):
        if antrian[i] == cari_angka:
            return True
    return False

antrian = deque([100, 50, 75, 25, 20, 45, 55, 30])

print('data sekarang: ',antrian)

print('=' * 25, 'MENAMBAH ANTREAN', '=' * 25)

#Menambahkan Antrean
antrian.append(15)
print('data masuk: ',15)
print('data sekarang: ',antrian)

antrian.append(35)
print('data masuk: ',35)
print('data sekarang: ',antrian)

antrian.append(60)
print('data masuk: ',60)
print('data sekarang: ',antrian)

print('=' * 25, 'MENGURANGI ANTREAN', '=' * 25)

#Mengurangi antrean
out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

#Mencari Data
cari_angka = int(input('\nMasukkan data yang akan dicari: ')) # Operasi mencari data

if cari(antrian, cari_angka):
    print('\nData', cari_angka, 'ditemukan!')
else:
    print('\nData tidak ditemukan!')
exit() 