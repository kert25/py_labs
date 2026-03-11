print("--- Калькулятор (введите 'выход' для завершения) ---")

while True:
    try:
        action = input("Выберите операцию (+, -, *, /) или 'выход': ").lower()
        
        if action == 'выход':
            print("Программа завершена.")
            break

        if action not in ('+', '-', '*', '/'):
            print("Ошибка: Неверная операция!")
            continue

        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))

        if action == '+':
            print(f"Результат: {num1 + num2}")
        elif action == '-':
            print(f"Результат: {num1 - num2}")
        elif action == '*':
            print(f"Результат: {num1 * num2}")
        elif action == '/':
            if num2 != 0:
                print(f"Результат: {num1 / num2}")
            else:
                print("Ошибка: Деление на ноль!")
        
        print("-" * 20)

    except ValueError:
        print("Ошибка: Вводите только числа!")
