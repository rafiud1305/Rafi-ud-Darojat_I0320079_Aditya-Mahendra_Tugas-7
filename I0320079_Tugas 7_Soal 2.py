print("===============================================================")
print("Soal 2 Tugas 7")
print("===============================================================")

import math
import random
def fungsinumerik(angka1,angka2,angka3):
    #Fungsi flooor
    print('\nFungsi Floor')
    print(angka1, 'menjadi', math.floor(angka1))
    print(angka2, 'menjadi', math.floor(angka2))
    print(angka3, 'menjadi', math.floor(angka3))
    #Fungsi Ceil
    print('\nFungsi Ceil')
    print(angka1, 'menjadi', math.ceil(angka1))
    print(angka2, 'menjadi', math.ceil(angka2))
    print(angka3, 'menjadi', math.ceil(angka3))
    #Fungsi Abs dan Fabs
    print('\nFungsi Abs dan Fabs')
    print(angka1, 'menjadi',abs(angka1))
    print(angka2, 'menjadi',abs(angka2))
    print(angka3, 'menjadi',abs(angka3))
    print(angka1, 'menjadi',math.fabs(angka1))
    print(angka2, 'menjadi',math.fabs(angka2))
    print(angka3, 'menjadi',math.fabs(angka3))
    #Nilai akhir
    print('\nMencari nilai Minimal dan Maksimal')
    print('nilai minimal dari ketiga angka adalah = ', min(angka1,angka2,angka3))
    print('nilai maksimal dari ketiga angka adalah = ', max(angka1,angka2,angka3))
    print('\nMemilih nilai random dengan choice')
    a = [angka1,angka2,angka3]
    print('a= ', a)
    print('Random 1')
    print('Pilih= ', random.choice(a))
    print('Random 2')
    print('Pilih= ', random.choice(a))
    print('Random 3')
    print('Pilih= ', random.choice(a))

print("Desimal menggunakan titik")
a = float(input("Ketik angka pertama:"))
b = float(input("Ketik angka kedua:"))
c = float(input("Ketik angka ketiga:"))
fungsinumerik(a,b,c)