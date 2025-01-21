def fib_rec(n,arr):
    if n <= 1:
        return n
    if (arr[n]) > 0:
        return arr[n]
    arr[n] = fib_rec(n-1,arr) + fib(n-2,arr)
    return arr[n]

def fib(n):
    arr = [0]*(n+1)
    arr[1]=1
    return fib_rec(n,arr)

# Not working for 100 percent
print(fib(3))