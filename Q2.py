def m(left, right):
    
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result



def bsearch(arr, x):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            
            return True
        
        elif arr[mid] < x:
            
            low = mid + 1
            
        else:
            
            high = mid - 1
            
    return False



def msort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = msort(left)
    right = msort(right)

    return m(left, right)



def findpairs(arr, target):
    
    arr = msort(arr)
    for i in arr:
        if bsearch(arr, target - i):
            print(f"{i}, {target - i})")
            
        
import time
import random
import matplotlib.pyplot as plt

def measuretime(n):
    
    S = [random.randint(1, 100) for _ in range(n)]
    target = random.randint(1, 200)
    
    start_time = time.time()
    findpairs(S, target)
    end_time = time.time()
    
    return end_time - start_time

n1 = list(range(1, 10)) + [10, 100, 1000, 10000, 100000, 1000000]
time1 = []

for n in n1:
    
    t = measuretime(n)
    time1.append(t)

plt.plot(n1, time1)
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Algorithm Scalability')
plt.show()
            


