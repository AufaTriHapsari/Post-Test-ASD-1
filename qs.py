import os 
import random
os.system('cls')

data= []
#tipe data yang digunakan list dengan rentang nilai 1 - 40
data = list(range(1,40)) 
#Pengambilan jumlah sample data yang diambil 10
acak = random.sample(data, k=10)

def partition(array, begin, end):
    print("Sorting :", acak)
    print("="*70)
    
    pivot = array[end]
    
# Pointer yang berfungsi untuk elemen yang lebih besar
    i = begin - 1
    
    for j in range(begin, end):
        if array[j] <= pivot:
            
            i = i + 1
            
            (array[i], array[j] ) = (array[j], array[i])
            
    (array[i + 1], array[end]) = (array[end], array[i+1])
    
    return i + 1

def quickSort(array, begin, end):
    if begin < end:
        
        ptc =  partition(array, begin, end)
        
        quickSort(array, begin, ptc - 1)
        
        quickSort(array, ptc + 1, end)
        
def listbaru(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
    
print("List Sebelum disort", acak)
print("-"*70)

quickSort(acak, 0 , len(acak) - 1)
print("List Setelah disort")
listbaru(acak)