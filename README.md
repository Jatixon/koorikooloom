# README.md

## Описание проекта

Этот проект содержит функции для вычисления тригонометрических, логарифмических и гиперболических значений с использованием разложений в ряды Тейлора. Основные функции представлены ниже.

## Функции

- `taylor_sin(x, terms=10)`: Вычисляет синус \( \sin(x) \) с использованием разложения в ряд Тейлора.
- `taylor_ln1_minus_x(x, terms=10)`: Вычисляет натуральный логарифм \( \ln(1-x) \) с использованием разложения в ряд Тейлора.
- `taylor_cosh(x, terms=10)`: Вычисляет гиперболический косинус \( \cosh(x) \) с использованием разложения в ряд Тейлора.

## Установка

1. Убедитесь, что у вас установлен Python.
2. Скопируйте файл с кодом на ваш компьютер.
3. Запустите программу с помощью команды:

    ```bash
    python main.py
    ```

## Использование

1. Запустите программу.
2. Выберите функцию в меню:
    - \( \sin(x) \)
    - \( \ln(1-x) \)
    - \( \cosh(x) \)
3. Введите значение \( x \) для вычисления (учитывайте граничные условия):
    - Для \( \sin(x) \): любое значение \( x \).
    - Для \( \ln(1-x) \): \( -1 < x \leq 1 \).
    - Для \( \cosh(x) \): любое значение \( x \).

## Чек-лист

- [ ] Убедиться, что Python установлен.
- [ ] Скачать файл `main.py`.
- [ ] Запустить программу.
- [ ] Проверить результаты вычислений.

## Примеры кода

Вот пример использования функции `taylor_sin` для вычисления значения синуса:

```python
x = math.radians(30)  # Преобразуем угол в радианы
result = taylor_sin(x, terms=10)
print(f"Приближенное значение синуса: {result}")
```

И пример для вычисления \( \ln(1-x) \):

```python
x = 0.5
result = taylor_ln1_minus_x(x, terms=10)
print(f"Приближенное значение ln(1-x): {result}")
```

## Примечания

- Программа содержит встроенные проверки на граничные условия для каждой функции.
- Рекомендуется использовать значение `terms` в диапазоне от 5 до 15 для достижения баланса между точностью и производительностью.
