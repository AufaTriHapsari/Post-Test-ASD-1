import os 
import random
os.system('cls')

data = []

def shellsort(data):
    n = len (data)
    gap = n // 2
        
    while gap > 0:
        for i in range (gap, n):
            temp = data[i]
            j=i
            while j >= gap and data [j-gap] > temp:
                data[j] = data[j-gap]
                j -= gap 
            data [j] = temp
        gap //= 2
    return data

#Tipe data yang digunakan rentan 2 - 80 dan Pemngambilan jumlah sample data yang diambil 10
data = [random.randint(2,80) for angka in range(10)]
print("Shell Sort")
print("="*70)
print("List Sebelum disort", data)
hasil = shellsort(data)
print("List Setelah disort", data)
print("="*70)