import math

# Константа: количество членов ряда Тейлора
TERMS = 10


def taylor_sin(x, terms=TERMS):
    """Вычисляет синус с помощью разложения в ряд Тейлора."""
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result


def taylor_ln1_minus_x(x, terms=TERMS):
    """Вычисляет ln(1-x) с помощью разложения в ряд Тейлора."""
    if x <= -1 or x > 1:
        raise ValueError("x должен быть в пределах -1 < x <= 1")

    result = 0
    for n in range(1, terms + 1):
        term = (-1) ** (n + 1) * (x ** n) / n
        result += term
    return result


def taylor_ch(x, terms=TERMS):
    """Вычисляет cosh(x) с помощью разложения в ряд Тейлора."""
    result = 0
    for n in range(terms):
        term = (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result


def taylor_pow(plus_x, m, terms=TERMS):
    """Вычисляет (1+x)^m с помощью разложения в ряд Тейлора."""
    if plus_x <= -1:
        raise ValueError("x должен быть больше -1")

    result = 1  # Первый член ряда
    current_term = 1
    for n in range(1, terms):
        current_term *= (m - (n - 1)) * plus_x / n
        result += current_term
    return result


def main_menu():
    while True:
        print("\nВыберите функцию:")
        print("1. sin(x)")
        print("2. ln(1-x)")
        print("3. cosh(x)")
        print("4. (1+x)^m")
        print("5. Выход")

        try:
            choice = int(input("Ваш выбор: "))
            if choice == 5:
                print("Выход из программы...")
                break

            x = float(input("Введите значение x: "))

            if choice == 1:  # sin(x)
                result = taylor_sin(x)
                actual = math.sin(x)
                print(f"Приближение: {result}")
                print(f"Реальное значение: {actual}")
                print(f"Разница: {abs(result - actual)}")

            elif choice == 2:  # ln(1-x)
                if not (-1 < x <= 1):
                    print("Ошибка: x должен быть в пределах -1 < x <= 1.")
                    continue
                result = taylor_ln1_minus_x(x)
                actual = math.log(1 - x)
                print(f"Приближение: {result}")
                print(f"Реальное значение: {actual}")
                print(f"Разница: {abs(result - actual)}")

            elif choice == 3:  # cosh(x)
                result = taylor_ch(x)
                actual = math.cosh(x)
                print(f"Приближение: {result}")
                print(f"Реальное значение: {actual}")
                print(f"Разница: {abs(result - actual)}")

            elif choice == 4:  # (1+x)^m
                m = float(input("Введите значение m: "))
                if x <= -1:
                    print("Ошибка: x должен быть больше -1.")
                    continue
                result = taylor_pow(x, m)
                actual = (1 + x) ** m
                print(f"Приближение: {result}")
                print(f"Реальное значение: {actual}")
                print(f"Разница: {abs(result - actual)}")

            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main_menu()
