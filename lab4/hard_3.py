def curry_add(a):
    def inner(b):
        return a + b
    return inner


def curry_multiply(a):
    def inner(b):
        return a * b
    return inner


add_5 = curry_add(5)
print(f"add_5(3) = {add_5(3)}")
print(f"add_5(10) = {add_5(10)}")

mul_3 = curry_multiply(3)
print(f"mul_3(4) = {mul_3(4)}")
print(f"mul_3(7) = {mul_3(7)}")
