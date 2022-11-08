def fibonacci(n):
    fib = [0, 1, 1]
    for x in range(3, n + 1):
        fib.append(fib[x-1] + fib[x-2])
    
    return fib[n]

print(fibonacci(11))