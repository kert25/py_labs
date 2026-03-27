numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))
cubes = list(map(lambda x: x**3, numbers))
doubled = list(map(lambda x: x * 2, numbers))

print(f"Исходный список: {numbers}")
print(f"Квадраты: {squares}")
print(f"Кубы: {cubes}")
print(f"Удвоенные: {doubled}")
