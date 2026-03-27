def sum_odd(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += i
    return s


n = 10
print(f"Сумма нечётных чисел от 1 до {n}: {sum_odd(n)}")
