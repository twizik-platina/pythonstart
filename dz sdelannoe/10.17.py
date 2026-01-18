n = int(input("Введите n: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

result = (2 * 5 * factorial + 3 * 8 * factorial) / (6 * factorial + 4 * factorial)

print(f"Результат: {result}")