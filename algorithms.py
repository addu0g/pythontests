
import math as m
def sortArray(arreglo):
    mElem = 0
    mIdx = 0
    for i in range(len(arreglo)-1):
        mElem = arreglo[i]
        mIdx = i
        for j in range(i+1,len(arreglo),1):
            if arreglo[j] < mElem :
                mElem = arreglo[j]
                mIdx = j
        tmp = arreglo[i]
        arreglo[i] = mElem
        arreglo[mIdx] = tmp
    return arreglo

def quickSearch(arreglo, value):
    low=0
    mid=0
    high= len(arreglo) 
    while(low <= high):
        mid = m.floor((low+high)/2) 
        if arreglo[mid-1] == value:
            return True
        elif arreglo[mid-1] > value:
            high = mid - 1
        else:
            low = mid + 1
    return False
    
def factorial(n):
    if n == 0 or n < 0:
        return 1
    else:
        tmp = n * factorial(n-1)
        return tmp
    

v = [1,2.2,5.5,2,3,6,8,5]
result = sortArray(v)
print(result)
exists = quickSearch(result, 15)
print(exists)

res = factorial(5)
print("factorial "+ str(res))
