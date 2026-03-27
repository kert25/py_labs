def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


n = 10
print(f"Первые {n} чисел Фибоначчи:")
print(fibonacci(n))
