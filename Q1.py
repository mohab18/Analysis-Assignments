def dandc(a, n):
    
    if n == 0:
        return 1
    
    if n % 2 == 0:
        x = dandc(a, n // 2)
        return x * x
    
    else:
        x = dandc(a, (n - 1) // 2)
        return x * x * a


def iterate(x, y):
    res = 1
    i = 1
    
    while i <= y:
        
        res *= x
        i += 1
        
    return res



import time
import matplotlib.pyplot as plt

def measure(func, *args):
    
    stime = time.time()
    result = func(*args)
    etime = time.time()
    elapsed = etime - stime
    return result, elapsed

n1 = list(range(1, 100001, 10000))
naive = []
conquer = []

for n in n1:
    
    _, naive = measure(iterate, 2, n)
    _, conquer = measure(dandc, 2, n)
    naive.append(naive)
    conquer.append(conquer)

plt.figure(figsize=(10, 6))
plt.plot(n1, naive, label='Naive Iterative Method')
plt.plot(n1, conquer, label='Divide-and-Conquer Method')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Algorithm Scalability')
plt.grid(True)
plt.show()
