import os 
import random
os.system('cls')

def mergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
            
kosong = [] 
print("Merge Sort")
list = list(range(1,30))
arr = random.sample(list, k=10)
print(f"List sebelum disortir {arr}")
mergeSort(arr)
print(f"List sesudah disortir {arr}")

