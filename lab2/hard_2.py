def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


num1 = 48
num2 = 18
print(f"НОД чисел {num1} и {num2} равен {gcd(num1, num2)}")
