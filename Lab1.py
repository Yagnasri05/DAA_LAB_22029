import time
import random 

def BS(n, arr):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
def SS(n,arr):
    for i in range(n):
        max=arr[0]
        pos=0
        for j in range (0,n-i):
            if(arr[j]>=max):
                max=arr[j]
                pos=j
        arr[pos]=arr[n-i-1]
        arr[n-i-1]=max
        
def IS(n,arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


n = int(input("Enter the number of elements: "))
arr = [random.randint(1, 1000) for _ in range(n)] 
strtBS=time.time()
BS(n, arr)
endtBS=time.time()
execution_timeBS=(endtBS-strtBS)*10**3
print("Time taken for BS:",execution_timeBS,"ms")
#print("Sorted Array:")
#print(*arr, sep=", ")

strtSS=time.time()
SS(n,arr)
endSS=time.time()
execution_SS=(endSS-strtSS)*10**3
print("Execution time of SS:",execution_SS,"ms")
#print("Sorted Array:")
#print(*arr, sep=", ")

strtIS=time.time()
IS(n,arr)
endIS=time.time()
execution_IS=(endIS-strtIS)*10**3
print("Execution time of IS:",execution_IS,"ms")
print("Sorted Array:")
print(*arr, sep=", ")